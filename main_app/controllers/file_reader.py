from base_app import http, exceptions
from main_app.repo import FileRepo


class FileReaderController:
    def __init__(self) -> None:
        self.repo = FileRepo()
        self.exceptions = exceptions
        self.request = http.Request
        self.response = http.Response()

    def read_line(self, request):
        id, line = self.request(
            request
        ).required('id', 'read_line')

        document = self.repo.get_by_keyword('id', id)
        
        try:
            line_number = int(line) - 1
            line = document.file.open(mode='r').readlines()[line_number]
        except ValueError:
            line = document.file.open(mode='r').read()

        return self.response.data_response(line)
