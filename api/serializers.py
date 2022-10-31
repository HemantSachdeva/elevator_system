from rest_framework.serializers import *
from .models import *


class ElevatorBlockSerializer(ModelSerializer):
    """
    This class defines the serializer for the ElevatorBlock model.
    """

    class Meta:
        model = ElevatorBlock
        fields = "__all__"


class ElevatorSerializer(ModelSerializer):
    """
    This class defines the serializer for the Elevator model.
    """

    class Meta:
        model = Elevator
        fields = [
            "elevator_id",
            "current_floor",
            "status",
            "working",
            "door_status",
            "elevator_block",
        ]
