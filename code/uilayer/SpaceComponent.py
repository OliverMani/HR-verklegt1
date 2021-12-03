class SpaceComponent:
    """Component sem er bil"""
    def __init__(self, width):
        self.width = width

    def __str__(self):
        return ' ' * self.width
