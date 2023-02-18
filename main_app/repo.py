from base_app import base_repo, models


class AuthRepo(base_repo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Code
        self.filter_fields = ['code', 'date_created', 'is_active']