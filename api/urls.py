from django.urls import path

from .views import *

urlpatterns = [
    path("get/elevatorblocks/", ElevatorBlockListView.as_view()),
    path("create/elevatorblock/", CreateElevatorBlockView.as_view()),
]
