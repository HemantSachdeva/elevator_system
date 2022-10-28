from django.db import models


class ElevatorBlock(models.Model):
    """
    This model represents a building or a block with elevators

    Attributes:
        block_name (str): The name of the building block
        floors (int): The number of floors in the building block
        elevators (int): The number of elevators in the building block
    """

    block_name = models.CharField(max_length=50)
    floors = models.IntegerField()
    elevators = models.IntegerField()

    def __str__(self):
        return (
            f"{self.block_name} has {self.floors} floors and {self.elevators} elevators"
        )
