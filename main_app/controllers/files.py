from django.db.utils import IntegrityError
from base_app import http, exceptions
from main_app.repo import FileRepo
from main_app.serializers.files_serializer import FileSerializer


class FileController:
    def __init__(self) -> None:
        self.repo = FileRepo()
        self.exceptions = exceptions
        self.request = http.Request
        self.response = http.Response()
        self.serializer = FileSerializer

    def get_files(self, request):
        id, keyword = self.request(
            request,
        ).opts('id', 'keyword')

        files = self.repo.getByIDOrKeyword(id, keyword)
        many = False if id else True

        serializer = self.serializer(files, many=many)
        return self.response.data_response(serializer.data)

    def upload(self, request):
        name, file = self.request(
            request,
            'POST'
        ).required('name', 'file')

        try:
            file_obj = self.repo.create(name=name, file=file)
        except IntegrityError:
            raise self.exceptions.FieldConflict('This File already exists')
        
        return self.response.message_response(f"'{file_obj.name}' created successfully")
