from rectangle import Rectangle
from square import Square

if __name__ == "__main__":
    r = Rectangle(2, 3)
    s = Square(5)

    print(r)
    print(s)

    print(f"Rectangle area: {r.area}")
    print(f"Square area: {s.area}")

    # LSP demo: molemaid saab kasutada Shape tüübina
    shapes = [Rectangle(4, 6), Square(3), Rectangle(1, 10)]
    print("\nKõikide kujundite pindalad:")
    for shape in shapes:
        print(f" - {shape} -> area: {shape.area}")