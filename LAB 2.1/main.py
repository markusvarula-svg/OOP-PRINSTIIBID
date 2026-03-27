class CodeBuilder:
    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []

    def add_field(self, name, value):
        self.fields.append((name, value))
        return self

    def __str__(self):
        lines = [f"class {self.class_name}:", "  def __init__(self):"]
        if self.fields:
            for name, value in self.fields:
                lines.append(f"    self.{name} = {value}")
        else:
            lines.append("    pass")
        return "\n".join(lines)

cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0