from django.urls import path
from .views import RegisterView, SignInView, UserDetailView


urlpatterns = [
  path('register/', RegisterView.as_view()),
  path('login/', SignInView.as_view()),
  path('profile/', UserDetailView.as_view())
]