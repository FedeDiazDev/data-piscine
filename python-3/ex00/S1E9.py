from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a generic world character."""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a character with a name and a survival status."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """Abstract method to change the character status to dead."""
        pass

class Stark(Character):
    """Class representing a member of the House Stark."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a Stark family member using the parent constructor."""
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """Changes the Stark character status from alive to dead."""
        self.is_alive = False

