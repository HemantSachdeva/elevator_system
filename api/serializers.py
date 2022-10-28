from rest_framework.serializers import *
from .models import *


class ElevatorBlockSerializer(ModelSerializer):
    """
    This class defines the serializer for the ElevatorBlock model.
    """

    class Meta:
        model = ElevatorBlock
        fields = "__all__"
