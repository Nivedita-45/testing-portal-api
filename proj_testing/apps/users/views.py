from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer
)

from .services.auth_service import register_user, login_user
from .services.user_service import get_all_users


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = register_user(serializer.validated_data)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = login_user(
            serializer.validated_data['email'],
            serializer.validated_data['password']
        )

        return Response({
            "user": UserSerializer(data["user"]).data,
            "tokens": data["tokens"]
        })


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = get_all_users()
        return Response(UserSerializer(users, many=True).data)