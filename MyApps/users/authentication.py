from django.conf import settings
from django.core import signing
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from .models import AppUser


TOKEN_SALT = "iot_security.app_user_auth"
TOKEN_MAX_AGE = 60 * 60 * 24 * 7


def create_auth_token(user):
    return signing.dumps({"user_id": user.pk}, salt=TOKEN_SALT)


class AppUserTokenAuthentication(BaseAuthentication):
    keyword = "Bearer"

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None

        if auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) != 2:
            raise exceptions.AuthenticationFailed("Token invalido.")

        try:
            token = auth[1].decode()
        except UnicodeError:
            raise exceptions.AuthenticationFailed("Token invalido.")

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        max_age = getattr(settings, "APP_USER_TOKEN_MAX_AGE", TOKEN_MAX_AGE)

        try:
            data = signing.loads(token, salt=TOKEN_SALT, max_age=max_age)
        except signing.SignatureExpired:
            raise exceptions.AuthenticationFailed("Token expirado.")
        except signing.BadSignature:
            raise exceptions.AuthenticationFailed("Token invalido.")

        try:
            user = AppUser.objects.get(pk=data["user_id"], is_active=True)
        except (KeyError, AppUser.DoesNotExist):
            raise exceptions.AuthenticationFailed("Usuario no encontrado o inactivo.")

        return user, token

    def authenticate_header(self, request):
        return self.keyword
