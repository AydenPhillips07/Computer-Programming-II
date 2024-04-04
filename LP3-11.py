class ClLP311:
  def __init__(self, Designing, Coding, Debugging, Testing):
    self.Designing = Designing
    self.Coding = Coding
    self.Debugging = Debugging
    self.Testing = Testing
    self._Time = 0
    self._percents = [0]*4  

  def __percent(self, number):
    return round((number/self._Time) * 100, 2)