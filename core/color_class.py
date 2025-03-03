class Color:
    RED = 1
    GREEN = 2
    BLUE = 3
    PINK = 4
    YELLOW = 5
    WHITE = 6

    @staticmethod
    def to_string(color):
        """
        Convert a color constant to its name.
        """
        color_names = {
            Color.RED: "Red",
            Color.GREEN: "Green",
            Color.BLUE: "Blue",
            Color.PINK: "Pink",
            Color.YELLOW: "Yellow",
            Color.WHITE: "White"
        }
        return color_names.get(color, "Unknown")