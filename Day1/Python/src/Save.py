from enum import Enum


class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    @staticmethod
    def from_str(label: str):
        label = label.lower()
        if label in ('l', 'left'):
            return Direction.LEFT
        elif label in ('r', 'right'):
            return Direction.RIGHT
        else:
            raise NotImplementedError(f"String {label} can not be converted to Direction enum.")


class Safe:

    def __init__(self):

        # Set initial value to 50
        self.dial = 50

    def rotating(self, direction: Direction, movement: int):
        """
        This method is used to rotate the dial of the save to each direction

        :param direction: Defines in which direction the dial should move.
        :param movement: Defines how much positions the dial should move
        :return:
        """
        # Rotating left
        if direction == Direction.LEFT:

            for x in range(movement):

                if self.dial == 0:
                    self.dial = 99
                else:
                    self.dial -= 1

        # Rotating right
        elif direction == Direction.RIGHT:

            for x in range(movement):

                if self.dial == 99:
                    self.dial = 0
                else:
                    self.dial += 1

        else:
            raise ValueError(f"Not supported direction {direction}")