from django.conf import settings
from django.contrib.auth.models import User

def UserModel():
    return User


def UserModelString():
    try:
        return settings.AUTH_USER_MODEL
    except AttributeError:
        return 'auth.User'


def UsernameField():
    return getattr(UserModel(), 'USERNAME_FIELD', 'username')
