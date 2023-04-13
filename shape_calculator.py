class Rectangle:
  shape = "Rectangle"

  def __init__(self, w, h):
    self.width = w
    self.height = h

  def get_area(self):
    return self.width * self.height

  def set_height(self, h):
    self.height = h

  def set_width(self, w):
    self.width = w

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ''
      for line in range(self.height):
        picture += self.width * '*'
        picture += '\n'
    return picture

  def get_amount_inside(self, figure):
    main = self.get_area()
    insider = figure.get_area()
    return int(main / insider)

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(
      self.height) + ")"


class Square(Rectangle):
  shape = "Square"

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, w):
    self.width = w
    self.height = w

  def set_height(self, h):
    self.width = h
    self.height = h

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
