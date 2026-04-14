class Specification:
    def is_satisfied(self, item):
        raise NotImplementedError

    def __and__(self, other):
        return AndSpecification(self, other)

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.args)

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class NameSpecification(Specification):
    def __init__(self, name):
        self.name = name

    def is_satisfied(self, item):
        return item.name.lower() == self.name.lower()