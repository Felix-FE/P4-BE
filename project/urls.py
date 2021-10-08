from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/launches/', include('launches.urls')),
    path('api/auth/', include('jwt_auth.urls'))
]
