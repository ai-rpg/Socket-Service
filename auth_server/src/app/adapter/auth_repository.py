from interface.i_auth_repository import IAuthRepository
from interface.i_couchbase_repository import ICouchbaseRepository
class AuthRepository(IAuthRepository, ICouchbaseRepository):

    def __init__(self, mangement_api_token):
        self.mangement_api_token = mangement_api_token

    def get_user_by_email(self, email):
        pass

    def create_user(self, email, password):
        pass
