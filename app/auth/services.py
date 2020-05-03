import base64

from flask_login import LoginManager
from injector import Injector

from app.users.repositories import UserRepository

login_manager = LoginManager()
user_repository = Injector().get(UserRepository)


@login_manager.user_loader
def load_user(username):
    return user_repository.get(username.decode('utf-8'))


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.args.get('api_key')
    if api_key:
        user = user_repository.get_by_api_key(api_key).first()
        if user:
            return user

    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = user_repository.get_by_api_key(api_key).first()
        if user:
            return user

    return None
