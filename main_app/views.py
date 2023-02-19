from rest_framework.views import APIView
from main_app import auth
from main_app.controllers.signin import SignInController
from main_app.controllers.files import FileController
from main_app.controllers.file_reader import FileReaderController


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
        self.controller = FileController()

    def post(self, request):
        return self.controller.upload(request)


class FileReaderView(GuardedView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = FileReaderController()

    def get(self, request):
        return self.controller.read_line(request)
