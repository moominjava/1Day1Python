class Car():

  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")

  def start(self):
    return f"Car with {self.wheels} wheels"


class Convertible(Car):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.time = kwargs.get("time", 10)

  def take_off(self):
    return "taking off"

class something(Convertible):
  pass

porshe = Convertible(color="green", price="$40")
print(porshe.color)