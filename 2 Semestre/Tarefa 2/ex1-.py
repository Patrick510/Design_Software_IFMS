from abc import ABC, abstractmethod

class ShapeAreaCalculator(ABC):
  def __init__(self, shape) -> None:
    self.shape = shape

  @abstractmethod
  def calculate_area(self):
    pass

class Rectangle(ShapeAreaCalculator):
  def calculate_area(self):
    return self.shape['widht'] * self.shape['height']

class Circle(ShapeAreaCalculator):
  def calculate_area(self):
    return 3.14 * self.shape['radius']**2

calculate = Rectangle({'widht': 3, 'height': 2})
calculate2 = Circle({'radius': 10})

print(calculate.calculate_area())
print(calculate2.calculate_area())