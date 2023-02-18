from rest_framework.views import APIView
from main_app import auth
from main_app.controllers.signin import SignInController


class GuardedView(APIView):
    authentication_classes = [auth.Auth]


class SignInView(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = SignInController()
    
    def post(self, request):
        return self.controller.gen_auth(request)


class FileManagementView(GuardedView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
