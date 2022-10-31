from django.urls import path

from .views import *

urlpatterns = [
    path("get/elevatorblocks/", ElevatorBlockListView.as_view()),
    path("create/elevatorblock/", CreateElevatorBlockView.as_view()),
    path("get/elevators/<int:block_id>/", ElevatorListView.as_view()),
    path("get/elevator/<int:elevator_id>/<int:block_id>/", ElevatorView.as_view()),
]
