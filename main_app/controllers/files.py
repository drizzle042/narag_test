from django.db.utils import IntegrityError
from base_app import http, exceptions
from main_app.repo import FileRepo
from main_app.schemas.file_upload_schema import FileUploadSchema


class FileController:
    def __init__(self) -> None:
        self.repo = FileRepo()
        self.exceptions = exceptions
        self.request_schema = FileUploadSchema()
        self.response = http.Response()

    def upload(self, request):
        data = self.request_schema.loads(request.data)

        try:
            file_obj = self.repo.create(**data)
        except IntegrityError:
            raise self.exceptions.FieldConflict('This File already exists')
        
        return self.response.message_response(f'{file_obj.name} created successfully')
