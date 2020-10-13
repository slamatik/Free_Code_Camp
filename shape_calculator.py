class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        """
        Returns area (width * height)
        :return: float
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Returns perimeter (2 * width + 2 * height)
        :return: float
        """
        return self.height * 2 + self.width * 2

    def get_diagonal(self):
        """
        Returns diagonal ((width ** 2 + height ** 2) ** .5)
        :return:
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        else:
            return f"{'*' * self.width}\n" * self.height

    def get_amount_inside(self):
        pass

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side

    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width

    def set_height(self, height):
        self.side = height
        self.width = height
        self.height = height

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.side})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
