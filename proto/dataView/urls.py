from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirectLiveData),
    path("live/", views.liveData, name="live")
]
