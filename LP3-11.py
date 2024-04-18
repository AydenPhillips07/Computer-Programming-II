class ClLP311:

  def __init__(self, Designing, Coding, Debugging, Testing):
    self.Designing = Designing
    self.Coding = Coding
    self.Debugging = Debugging
    self.Testing = Testing
    self._Time = 0
    self._percents = [0] * 4

  def __percent(self, number):
    return round((number / self._Time) * 100, 2)

  def calculate(self):
    self._Time = self.Designing + self.Coding + \
     self.Debugging + self.Testing

    self._percents[0] = self.__percent(self.Designing)
    self._percents[1] = self.__percent(self.Coding)
    self._percents[2] = self.__percent(self.Debugging)
    self._percents[3] = self.__percent(self.Testing)

  def display(self):
    print("Task\t\t% Time")
    print(f"Designing\t\t\t{self._percents[0]}%")
    print(f"Coding\t\t{self._percents[1]}%")
    print(f"Debugging\t{self._percents[2]}%")
    print(f"Testing\t\t\t{self._percents[3]}%")

  def main():
    print("Enter the amount of time spent doing the following in minutes: \n")
    Designing = float(input("Designing: "))
    Coding = float(input("Coding: "))
    Debugging = float(input("Debugging: "))
    Testing = float(input("Testing: "))
    print()

  Time = ClLP311(Designing, Coding, Debugging, Testing)
  Time.calculate()
  Time.display()

  pass

  if __name__ == "__main__":
    main()
