from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError

from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as s

from .serializers import AppUserSerializer, AppUser
from .interfaces import UserData


"""
This class will be utilized through out the application for all
API endpoints that require Token Authentication for all logged 
in users. The vision for this application is to have both publicly
available information and user owned workouts and exercises.
"""
class Permissions(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


"""
The `Registration` class will be utilized to handle
requests for both returning users attempting to login
and acquire their token or new users signing up and
logging in for the first time to include acquiring 
a user token
"""
class Registration(APIView):

    def post(self, request:Request) -> Response:
        try:
            data: UserData = request.data.copy()
            user = authenticate(
                request=request,
                username=data.get("email"),
                password=data.get("password"),
            )
            if not user:
                user = self.sign_up(data)
            user_token, _ = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response(
                {"user": AppUserSerializer(user).data, "token": user_token.key},
                status=s.HTTP_201_CREATED if _ else s.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(e.message, status=s.HTTP_400_BAD_REQUEST)

    def sign_up(self, data: UserData) -> AppUser | ValidationError:
        data["username"] = data.get("email")
        new_user = AppUserSerializer(data=data)
        if new_user.is_valid():
            user = new_user.create(data)
            return user
        raise ValidationError(new_user.errors)
