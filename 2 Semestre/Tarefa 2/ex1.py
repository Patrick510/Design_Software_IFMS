class ShapeAreaCalculator:
  def calculate_area(self, shape):
    if shape['type'] == "rectangle":
      return shape['widht'] * shape['height']
    elif shape['type'] == ['circle']:
      return 3.14 * shape['radius']**2
    else:
      return None

rectangle = {'type': 'rectangle', 'widht': 2, 'height': 3}
circle = {'type': 'circle', 'radius': 5}

calculator = ShapeAreaCalculator()
print(calculator.calculate_area(rectangle))
print(calculator.calculate_area(circle))