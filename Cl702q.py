class Vehicle:
  def __init__(self, name, numTir, worth):
    self._name = name
    self._numTir = numTir
    self.worth = worth

  def getinfo(self):
    return self._name + " " + self._numTir

class Car(Vehicle):
  def __init__(self, name, numTir, worth):
    super().__init__(name, numTir, worth)
    

class Truck(Vehicle):
  def __init__(self, name, numTir, Mile, worth):
    super().__init__(name, numTir, worth)
    self.Mile = Mile
    


class Bus(Vehicle):
  def __init__(self, name, numTir, City, worth):
    super().__init__(name, numTir, worth)
    self.City = City
    