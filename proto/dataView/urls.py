from django.urls import path
from . import views

urlpatterns = [
    path("/", views.redirectLiveData, name="live"),
    path("/live", views.liveData)
]