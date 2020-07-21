from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import update_session_auth_hash
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import NotAuthenticated, IsOwnerOrSuper

# Create your views here.



# class UserRegisterAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     #permission_classes = (IsOwner,)

# class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     #permission_classes = (IsOwner,)
#     lookup_field = 'pk'

# class UserUpdateAPIView(APIView):
#     #permission_classes = (IsAuthenticated,)

#     def get_object(self):
#         return self.request.user

    # def put(self, request, *args, **kwargs):
#         self.object = self.request.user

#         serializer = ChangePasswordSerializer(data = request.data)

#         if serializer.is_valid():
#             print(serializer.data)
#             old_password = serializer.data.get("old_password")
#             if not self.object.check_password(old_password):
#                 return Response({"old_password": "wrong_password"}, status=status.HTTP_400_BAD_REQUEST)

#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             update_session_auth_hash(request, self.object)
#             return Response(status = status.HTTP_204_NO_CONTENT)

#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create user
class UserRegisterAPIView(generics.CreateAPIView):
    model = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]

class UpdatePassword(APIView):
    permission_classes = (IsOwnerOrSuper,)

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.request.user

        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": "wrong_password"}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)
            return Response(status = status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)