class Vehicle:
  def __init__(self, name, numTir):
    self._name = name
    self._numTir = numTir

  def getinfo(self):
    return self._name + " " + self._numTir

class Car(Vehicle):
  def __init__(self, name, numTir, value):
    super().__init__(name, numTir)
    self.value = value

class Truck(Vehicle):
  def __init__(self, name, numTir, Mile, worth):
    super().__init__(name, numTir)
    self.Mile = Mile
    self.worth = worth


class Bus(Vehicle):
  def __init__(self, name, numTir, City):
    super().__init__(name, numTir)
    self.City = City