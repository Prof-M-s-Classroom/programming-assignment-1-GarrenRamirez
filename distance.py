from datetime import datetime

class Distance:
    """
    Class to represent a distance measurement with timestamp.
    """
    
    def __init__(self, distance: float):
        """Initialize the Distance object with distance and timestamp."""
        self.distance = distance
        self.timestamp = datetime.now().strftime("%H:%M:%S")

    def __str__(self):
        """Return a formatted string representation of the Distance object."""
        return f"{self.distance} centimeters recorded at {self.timestamp}"
