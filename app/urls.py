
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('', include("login.urls")),
    path('user/', include("users.urls")),
    path('admin/', include("admins.urls")),
]
