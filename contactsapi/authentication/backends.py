import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        # print(auth_data.decode('utf-8'))
        prefix, token = auth_data.decode('utf-8').split(' ')
        # print(jwt.decode(token, settings.JWT_SECRET_KEY))

        # try:
        payload = jwt.decode(token, 'None')
        print(payload)


            # user = User.objects.get(username=payload['username'])
            # return (user, token)

        # except jwt.DecodeError as identifier:
        #     raise exceptions.AuthenticationFailed(
        #         'Your token is invalid,logins')
        # except jwt.ExpiredSignatureError as identifier:
        #     raise exceptions.AuthenticationFailed(
        #         'Your token is expired,login')

        return super().authenticate(request)