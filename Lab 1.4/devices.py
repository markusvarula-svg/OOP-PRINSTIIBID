from interfaces import Printer, Scanner, Fax


class MyPrinter(Printer):
    def print(self, document):
        print(f"[MyPrinter] Printing: {document}")

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"[Photocopier] Printing: {document}")

    def scan(self, document):
        print(f"[Photocopier] Scanning: {document}")

class MultiFunctionMachine(Printer, Scanner):
    def __init__(self, printer: Printer, scanner: Scanner):
        self._printer = printer
        self._scanner = scanner

    def print(self, document):
        self._printer.print(document)

    def scan(self, document):
        self._scanner.scan(document)