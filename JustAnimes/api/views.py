from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .serializers import UserSerializer, UserConnecterSerializer
from.models import User
from rest_framework.response import Response


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SeConnecterView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs) -> Response:
        try:
            user = User.objects.get(mail = request.data.get('mail'),
                mdp = request.get('mdp'))
            return Response({"msg": "trouvé", "user": self.serializer_class(user).data}, status = status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
