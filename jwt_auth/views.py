from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import SignUpSerializer, UserDetailSerializer
User = get_user_model()
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):

  def post(self, request):
    user_to_create = SignUpSerializer(data=request.data)
    if user_to_create.is_valid():
      user_to_create.save()
      return Response(
        {'message':'Sign-Up Successful'},
        status=status.HTTP_201_CREATED
      )
    return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class SignInView(APIView):

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
      user_to_LogIn = User.objects.get(username=username)
    except User.DoesNotExist:
      raise PermissionDenied(detail='Unauthorized username')

    if not user_to_LogIn.check_password(password):
      raise PermissionDenied(detail='Unauthorized password')

    expiry_time = datetime.now() + timedelta(days=7)
    token = jwt.encode(
      {'sub':user_to_LogIn.id, 'exp': int(expiry_time.strftime('%s'))},
      settings.SECRET_KEY,
      algorithm='HS256'
    )
    
    return Response({
      'token': token,
      'message': f'welcome back {username}'
    }, status=status.HTTP_200_OK)
  

class UserDetailView(APIView):

  permission_classes = (IsAuthenticated, )

  def get(self, request):
    serialized_user = UserDetailSerializer(request.user)
    return Response(serialized_user.data, status=status.HTTP_200_OK)