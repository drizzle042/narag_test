from base_app import http, exceptions
from main_app.repo import FileRepo


class FileReaderController:
    def __init__(self) -> None:
        self.repo = FileRepo()
        self.exceptions = exceptions
        self.request = http.Request
        self.response = http.Response()

    def read_line(self, request):
        file_name, line = self.request(
            request
        ).required('file_name', 'read_line')

        document = self.repo.get_by_keyword('name', file_name)

        if str(line).lower() == 'all':
            line = document.file.open(mode='r').read()
        else:
            try:
                line_number = int(line) - 1
            except ValueError:
                raise exceptions.WrongFieldType(
                    "'line' must be 'all' or a positive integer"
                )
            line = document.file.open(mode='r').readlines()[line_number]

        return self.response.data_response(line)
