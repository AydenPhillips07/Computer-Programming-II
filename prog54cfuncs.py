def calcArea(pi, radius):
  return pi * radius**2

def calcCirc(pi, radius):
  return 2 * pi * radius

def areaCirc(pi, radius):
  area = calcArea(pi, radius)
  circ = calcCirc(pi, radius)
  return area, circ

def main():
  pi = 3.1459
  radius = float(input("Enter Radius :"))
  


if __name__ == "__main__":
  main()