from werkzeug.security import safe_str_cmp

from codebase.models.usermodel import UserModel


users = [
    UserModel(1, 'bob', 'whatever_password')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id)
