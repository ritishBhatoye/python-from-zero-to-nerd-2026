"""Exercise 86 — Class vs Instance Attributes.

Your implementation goes here.
"""


class Person:
    """Demonstrate class vs instance attributes."""
    
    # Class attribute (shared by all instances)
    species = "Human"
    
    def __init__(self, name: str | None = None):
        """
        Initialize with optional name.
        
        Args:
            name: Person's name (instance attribute)
        """
        pass


def demonstrate_attributes() -> dict[str, str]:
    """
    Create two Person instances and return their attributes.
    
    Returns:
        Dictionary showing class attribute vs instance attributes
    """
    pass
