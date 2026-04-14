from shape import Shape

class Square(Shape):
    def __init__(self, size):
        self.size = size

    @property
    def area(self):
        return self.size * self.size

    def __str__(self):
        return f"Square(size={self.size})"