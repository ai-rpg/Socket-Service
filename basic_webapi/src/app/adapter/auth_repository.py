from interface.i_auth_repository import IAuthRepository

class AuthRepository(IAuthRepository):

    def __init__(self, mangement_api_token):
        self.mangement_api_token = mangement_api_token

    def get_user_by_email(self, email):
        pass

    def create_user(self, email, password):
        pass
