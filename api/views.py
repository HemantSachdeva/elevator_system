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
