# from django.conf.urls import url
from django.urls import  path

from .views import VideoListApiView

urlpatterns = [
    path("list", VideoListApiView.as_view({"get": "list"})),
]
