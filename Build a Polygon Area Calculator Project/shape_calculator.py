class Rectangle:
    """
    Represents a rectangular shape defined by its width and height.
    Provides methods to calculate geometrical properties and a string
    representation.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object.

        Args:
            width (int/float): The width of the rectangle.
            height (int/float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def set_height(self, height):
        """
        Sets the height of the rectangle to a new value.

        Args:
            height (int/float): The new height for the rectangle.
        """
        self.height = height

    def set_width(self, width):
        """
        Sets the width of the rectangle to a new value.

        Args:
            width (int/float): The new width for the rectangle.
        """
        self.width = width

    def get_area(self):  # A = height x width
        """
        Calculates the area of the rectangle.

        Returns:
            int/float: The calculated area.
        """
        return self.height * self.width

    def get_perimeter(self):  # P = 2 x (height + width)
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int/float: The calculated perimeter.
        """
        return 2 * (self.height + self.width)

    def get_diagonal(self):  # d = (width^2 + height^2)^0.5
        """
        Calculates the length of the diagonal of the rectangle.

        Returns:
            float: The calculated diagonal length.
        """
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        """
        Generates a string representation of the rectangle using '*' characters.
        The picture will have 'height' rows, each with 'width' asterisks,
        followed by a newline character.

        Returns:
            str: The visual representation of the rectangle, or
                 'Too big for picture.' if dimensions exceed 50.
        """
        # Check if the dimensions are too large for a picture
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""  # Initialize an empty string to build the picture

        # Loop 'height' times to create each row of the picture
        for _ in range(self.height):
            # Concatenate 'width' asterisks and a newline character for each row
            picture += ("*" * self.width) + "\n"

        return picture

    def get_amount_inside(self, shape):
        """
        Calculates how many times another given shape (Rectangle or Square)
        can fit completely inside this rectangle without rotation.

        Args:
            shape (Rectangle/Square): The shape object to fit inside.

        Returns:
            int: The number of times the 'shape' can fit.
        """
        # Calculate how many times the 'shape's width fits into this rectangle's width
        width_fits = self.width // shape.width
        # Calculate how many times the 'shape's height fits into this rectangle's height
        height_fits = self.height // shape.height

        # The total amount is the product of horizontal and vertical fits
        return width_fits * height_fits

    def __str__(self):
        """
        Returns a string representation of the Rectangle object for printing.

        Returns:
            str: A formatted string like 'Rectangle(width=X, height=Y)'.
                 The width and height are cast to int to ensure consistent
                 integer representation in the string.
        """
        return f"Rectangle(width={int(self.width)}, height={int(self.height)})"


class Square(Rectangle):
    """
    Represents a square shape. Inherits from Rectangle, ensuring its
    width and height are always equal.
    """

    def __init__(self, side):
        """
        Initializes a new Square object.

        Args:
            side (int/float): The length of the side of the square.
        """
        # Call the constructor of the parent class (Rectangle)
        # A square's width and height are always equal to its side.
        super().__init__(side, side)
        self.side = side  # Store the side attribute specifically for Square

    def set_side(self, side):
        """
        Sets the side length of the square. This also updates the
        inherited width and height to maintain the square property.

        Args:
            side (int/float): The new side length for the square.
        """
        self.side = side
        self.width = side  # Update inherited width
        self.height = side  # Update inherited height

    def set_width(self, width):
        """
        Overrides the set_width method from Rectangle.
        For a Square, changing the width means changing its side,
        which in turn updates both width and height.

        Args:
            width (int/float): The new width (and side) for the square.
        """
        self.set_side(width)  # Delegate to set_side to ensure consistency

    def set_height(self, height):
        """
        Overrides the set_height method from Rectangle.
        For a Square, changing the height means changing its side,
        which in turn updates both width and height.

        Args:
            height (int/float): The new height (and side) for the square.
        """
        self.set_side(height)  # Delegate to set_side to ensure consistency

    def __str__(self):
        """
        Returns a string representation of the Square object for printing.

        Returns:
            str: A formatted string like 'Square(side=X)'.
                 The side is cast to int to ensure consistent integer
                 representation in the string.
        """
        return f"Square(side={int(self.side)})"  # Cast to int for output consistency


def main():
    """
    Demonstrates the usage of the Rectangle and Square classes as specified
    in the project requirements. Prints various properties and string representations.
    """
    # Usage example:
    # Create a Rectangle object
    rect = Rectangle(10, 5)
    print(rect.get_area())

    # Modify the rectangle's height and calculate its perimeter
    rect.set_height(3)
    print(rect.get_perimeter())

    # Print the string representation of the rectangle
    print(rect)

    # Get the visual picture representation of the rectangle
    print(rect.get_picture())

    # Create a Square object
    sq = Square(9)
    print(sq.get_area())

    # Modify the square's side and calculate its diagonal
    sq.set_side(4)
    print(sq.get_diagonal())

    # Print the string representation of the square
    print(sq)

    # Get the visual picture representation of the square
    print(sq.get_picture())

    # Prepare the rectangle for testing get_amount_inside
    rect.set_height(8)
    rect.set_width(16)

    # Calculate how many squares (sq) fit inside the rectangle (rect)
    print(rect.get_amount_inside(sq))

    # Expected output for this code:
    # 50
    # 26
    # Rectangle(width=10, height=3)
    # **********
    # **********
    # **********
    # 81
    # 5.656854249492381
    # Square(side=4)
    # ****
    # ****
    # ****
    # ****
    # 8


if __name__ == "__main__":
    main()
