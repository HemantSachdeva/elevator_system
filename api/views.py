from rest_framework.generics import *

from .models import *
from .serializers import *


def create(elevators: int, block_id: int):
    """
    This method creates n number of elevators for the elevator block

    Args:
        elevators (int): The number of elevators to create
        block_id (int): The id of the elevator block to create the elevators for
    """
    for elevator in range(elevators):
        Elevator.objects.create(
            elevator_id=elevator, elevator_block=ElevatorBlock.objects.get(id=block_id)
        )


class CreateElevatorBlockView(CreateAPIView):
    """
    This class creates a new elevator block or building
    """

    serializer_class = ElevatorBlockSerializer

    def perform_create(self, serializer):
        serializer.save()

        # Create elevators for the elevator block
        create(serializer.data["elevators"], serializer.data["id"])


class ElevatorBlockListView(ListAPIView):
    """
    This class lists all the elevator blocks
    """

    queryset = ElevatorBlock.objects.all()
    serializer_class = ElevatorBlockSerializer


class ElevatorListView(ListAPIView):
    """
    This class lists all the elevators in the given elevator block
    """

    serializer_class = ElevatorSerializer

    def get_queryset(self):
        return Elevator.objects.filter(elevator_block=self.kwargs["block_id"])


class ElevatorView(RetrieveAPIView):
    """
    This class gets the elevator with the given elevator id and elevator block id
    """

    serializer_class = ElevatorSerializer

    def get_object(self):
        return Elevator.objects.get(
            elevator_id=self.kwargs["elevator_id"],
            elevator_block=self.kwargs["block_id"],
        )


class UpdateElevatorView(UpdateAPIView):
    """
    This class updates the elevator with the given elevator id and elevator block id
    """

    serializer_class = ElevatorSerializer

    def get_object(self):
        return Elevator.objects.get(
            elevator_id=self.kwargs["elevator_id"],
            elevator_block=self.kwargs["block_id"],
        )

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
