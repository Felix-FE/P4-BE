from django.urls import path 
from .views import (
  CreateUpdateView,
  EditVerifyUpdateView,
  LaunchFollowView,
  LaunchListView,
  LaunchDetailView,
  RemoveUpdateView,
)

urlpatterns = [
  path('',LaunchListView.as_view()),
  path('<int:pk>/', LaunchDetailView.as_view()),
  path('<int:launch_pk>/updates/', CreateUpdateView.as_view()),
  path('<int:launch_pk>/updates/<int:update_pk>', RemoveUpdateView.as_view()),
  path('<int:launch_pk>/follow/', LaunchFollowView.as_view()),
  path('<int:launch_pk>/updates/<int:update_pk>/<str:verify_id>/', EditVerifyUpdateView.as_view()),
]

