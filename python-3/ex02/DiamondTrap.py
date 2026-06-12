from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing King Joffrey, born from a diamond inheritance conflict."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the King using MRO, which defaults to Baratheon traits."""
        super().__init__(first_name, is_alive)
        if hasattr(self, "hairs"):
            delattr(self, "hairs")
        self.hair = "dark"

    def get_eyes(self) -> str:
        """Getter for the eyes attribute."""
        return self.eyes

    def set_eyes(self, color: str) -> None:
        """Setter to change the eyes attribute."""
        self.eyes = color

    def get_hairs(self) -> str:
        """Getter for the hairs attribute."""
        return getattr(self, "hairs", getattr(self, "hair", "dark"))

    def set_hairs(self, color: str) -> None:
        """Setter to change the hair attribute to plural 'hairs' as expected."""
        if hasattr(self, "hair"):
            delattr(self, "hair")
        self.hairs = color

    @property
    def eyes_prop(self) -> str:
        """Property for eyes."""
        return self.eyes

    @eyes_prop.setter
    def eyes_prop(self, color: str) -> None:
        self.eyes = color