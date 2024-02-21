def calcArea(pi, radius):
  return round(pi * radius**2, 2)

def calcCirc(pi, radius):
  return round(2 * pi * radius, 2)

def areaCirc(pi, radius):
  area = calcArea(pi, radius)
  circ = calcCirc(pi, radius)
  return area, circ

def main():
  pi = 3.1459
  radius = float(input("Enter Radius: "))
  a, c = areaCirc(pi, radius)
  print(f"Area: {a}\nCircumference: {c}")
  pass


if __name__ == "__main__":
  main()