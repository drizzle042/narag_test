from base_app import http
from main_app.auth import Auth


class SignInController:
    def __init__(self) -> None:
        self.auth = Auth()
        self.request = http.Request
        self.response = http.Response()

    def gen_auth(self, request):
        code, = self.request(
            request,
            'POST'
        ).required('code')

        auth = self.auth.check_code(code).gen_token_from_code()

        return self.response.data_response({'authToken': auth.token})
        