import random
cn = random.randint(1, 20)
pn = int(input("Enter a number between 1 and 20!:  "))
if cn == pn:
  print("Computer's Number: ", cn)
  print("Your Number: ", pn)
  print("You Won!")
else:
  print("Computer's Number: ", cn)
  print("Your Number: ", pn)
  print("Better Luck Next Time!")