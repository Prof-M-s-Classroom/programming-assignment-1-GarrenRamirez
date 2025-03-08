from datetime import datetime

class Distance:
    """
    Class to represent a distance measurement with timestamp.
    """
    def __init__(self, distance: float, timestamp: str = datetime.now().strftime("%M: %S")):
        """Initialize the Distance object with distance and timestamp."""
        self.distance = distance
        self.timestamp = timestamp

    def __str__(self):
        """Return a formatted string representation of the Distance object."""
        return f"{self.distance} centimeters recorded at {self.timestamp}"
