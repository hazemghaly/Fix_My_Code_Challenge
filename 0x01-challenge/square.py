#!/usr/bin/python3

class Square:
    """class"""

    def __init__(self, width=0, height=0):
        """Initializes"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """The area of the square."""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Cal the perimeter."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
