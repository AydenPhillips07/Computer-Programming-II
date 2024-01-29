
def main():
  j = int(input("Number of eggs: "))
  g = j // 12
  t = g * 12
  e = j - t
  if g < 4:
    a =  e * 0.042 + g * 0.5
    #y = round(a, 2)
    print("The bill is equal to: $", a)
  elif g >= 4 and g < 6:
    a = e * 0.038 + g * 0.45
   # y = round(a, 2)
    print("The bill is equal to: $", a)
  elif g >= 6 and g < 11:
    a = e * 0.033 + g * 0.4
    #y = round(a, 2)
    print("The bill is equal to: $", a) 
  elif g >= 11:
    a = e * 0.029 + g * 0.35
    #y = round(a, 2)
    print("The bill is equal to: $", a) 
  else:
    print("Invalid Input")





if __name__ == "__main__":
  main()
  