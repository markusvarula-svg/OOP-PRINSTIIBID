from shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"