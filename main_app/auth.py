from datetime import datetime, timedelta
import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from base_app import exceptions, models
from main_app import repo

class Auth(BaseAuthentication):
    def __init__(self) -> None:
        super().__init__()
        self.jwt = jwt
        self.model = models.Code
        self.repo = repo.AuthRepo()

    def check_code(self, code = None):
        if code is None:
            code = self.code

        try:
            code_obj = self.repo.get_by_keyword("code", code)
        except self.model.DoesNotExist:
            raise exceptions.NotFound("Wrong code, please check and try again")

        if code_obj.is_active:
            self.code_obj = code_obj
        else:
            raise exceptions.DiscontinuedCodeResponse

        return self

    def gen_token_from_code(self, code_obj = None, exp_time=8):
        if code_obj is None:
            code_obj = self.code_obj

        payload = {
            "ID": code_obj.code,
            "exp": datetime.utcnow() + timedelta(hours=exp_time)
        }

        token = self.jwt.encode(
            payload=payload,
            key=settings.SECRET_KEY,
            algorithm=settings.CRYPTOGRAPHIC_ALGORITHM
        )

        self.token = token

        return self

    def get_code_from_token(self, token = None):
        if token is None:
            token = self.token

        try:
            payload = self.jwt.decode(
                token,
                key=settings.SECRET_KEY,
                algorithms=[settings.CRYPTOGRAPHIC_ALGORITHM]
            )
        except self.jwt.exceptions.ExpiredSignatureError:
            raise exceptions.TokenExpired
        except self.jwt.exceptions.InvalidTokenError:
            raise exceptions.InvalidToken

        self.code = payload.get("ID")

        return self

    def authenticate(self, request):
        try:
            authorization = request.headers["authorization"]
        except KeyError:
            raise exceptions.FieldRequired("An authorization key in header is required")
        [*_, token] = authorization.split()
        auth = self.get_code_from_token(token).check_code()
        return auth.code_obj, token
        