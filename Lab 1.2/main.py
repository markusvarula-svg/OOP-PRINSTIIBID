from product import Product, Color, Size
from specification import ColorSpecification, SizeSpecification, NameSpecification
from filter import BetterFilter
 
if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)
 
    products = [apple, tree, house]
 
    bf = BetterFilter()
 
    print("Green products:")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")
 
    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")
 
    print("Large blue items:")
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")
 
    print("Product named Apple:")
    named = NameSpecification("Apple")
    for p in bf.filter(products, named):
        print(f" - {p.name} found by name")