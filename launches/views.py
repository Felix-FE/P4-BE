from rest_framework.generics import (
  ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)

from .serializers import LaunchSerializer, UpdateSerializer
from .models import Launch, Update
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from rest_framework.permissions import (
  IsAuthenticatedOrReadOnly, IsAuthenticated
)

class LaunchFollowView(APIView):

  permission_classes = (IsAuthenticated, )

  def post(self, request, launch_pk):
    try:
      launch_to_follow = Launch.objects.get(pk=launch_pk)
    except Launch.DoesNotExist:
      raise NotFound() 
    
    if request.user in launch_to_follow.followed_by.all():
      launch_to_follow.followed_by.remove(request.user.id)
    else: 
      launch_to_follow.followed_by.add(request.user.id)

    serialized_launch = LaunchSerializer(launch_to_follow)
    
    return Response(serialized_launch.data, status=status.HTTP_202_ACCEPTED)
  

class CreateUpdateView(APIView):

  permission_classes = (IsAuthenticated, )

  def post(self, request, launch_pk):
    request.data['launch'] = launch_pk
    request.data['owner'] = request.user.id
    created_update = UpdateSerializer(data=request.data)
    if created_update.is_valid():
      created_update.save()
      return Response(created_update.data, status=status.HTTP_201_CREATED)
    return Response(created_update.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RemoveUpdateView(APIView):

  permission_classes = (IsAuthenticated, )

  def delete(self, _request, **kwargs):
    update_pk = kwargs['update_pk']
    try:
      update_to_delete = Update.objects.get(pk=update_pk)
      update_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    except Update.DoesNotExist:
      raise NotFound(detail='Update Not Found')


class EditVerifyUpdateView(APIView):

  permission_classes = (IsAuthenticated, )

  def post(self, request, **kwargs):
    update_pk = kwargs['update_pk']
    try:
      update_to_verify = Update.objects.get(pk=update_pk)
      if kwargs['verify_id'] == 'reliable':
        if request.user in update_to_verify.reliable.all():
          update_to_verify.reliable.remove(request.user.id)
        else:
          update_to_verify.reliable.add(request.user.id)
      elif kwargs['verify_id'] == 'unreliable':
        if request.user in update_to_verify.unreliable.all():
          update_to_verify.unreliable.remove(request.user.id)
        else:
          update_to_verify.unreliable.add(request.user.id)
      elif kwargs['verify_id'] == 'official':
        if request.user in update_to_verify.official.all():
          update_to_verify.official.remove(request.user.id)
        else:
          update_to_verify.official.add(request.user.id)
      elif kwargs['verify_id'] == 'false':
        if request.user in update_to_verify.false.all():
          update_to_verify.false.remove(request.user.id)
        else:
          update_to_verify.false.add(request.user.id)
    except Update.DoesNotExist:
      raise NotFound()

    serialized_update = UpdateSerializer(update_to_verify)

    return Response(serialized_update.data, status=status.HTTP_202_ACCEPTED)  

# this shows the list of launches as well as adding new launches (for launch list page)
class LaunchListView(ListCreateAPIView):
  queryset = Launch.objects.all()
  serializer_class = LaunchSerializer
  permission_classes = (IsAuthenticatedOrReadOnly, )


# this gets a single Launch view as well as being able to update, delete or get a launch (for launch page)
class LaunchDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Launch.objects.all()
  serializer_class = LaunchSerializer
  permission_classes = (IsAuthenticatedOrReadOnly, )
