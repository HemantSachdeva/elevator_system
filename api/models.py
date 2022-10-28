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


class Elevator(models.Model):
    """
    The Elevator model is the main model for the application.

    Attributes:
        elevator_id (int) : The unique identifier for the elevator
        elevator_block (str) : The elevator block/building name that the elevator belongs to
        current_floor (int) : The current floor the elevator is on
        status (int) : The status of the elevator. It can be either "idle", "going up", or "going down" and the numbers 0, 1 and -1 assigned to it respectively
        working (bool) : A boolean field that indicates whether the elevator is working or not
        door_status (bool) : A boolean field that indicates whether the elevator door is open or closed
    """

    class Status(models.IntegerChoices):
        """
        The Status model is a helper model for the Elevator model.

        Attributes:
            IDLE (int) : The elevator is idle
            GOING_UP (int) : The elevator is going up
            GOING_DOWN (int) : The elevator is going down
        """

        IDLE = 0
        MOVING_UP = 1
        MOVING_DOWN = -1

    elevator_id = models.IntegerField()
    elevator_block = models.ForeignKey(ElevatorBlock, on_delete=models.CASCADE)
    current_floor = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices, default=Status.IDLE)
    working = models.BooleanField(default=True)
    door_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Elevator {self.elevator_id} is on floor {self.current_floor} and is {self.status}"
