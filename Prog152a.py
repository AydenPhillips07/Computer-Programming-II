import sys
sys.setrecursionlimit(5000)

def factLoop():
  product = 1
  for num in range(9669, 3, -3):
    product *= num
  return product

def main():
  print(product)
  if __name__ == "__name__":
    main()

