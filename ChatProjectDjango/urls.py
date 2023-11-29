from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path("chat/", include("chat.urls")),
]
