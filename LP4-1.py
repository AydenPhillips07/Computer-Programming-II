copies = int(input("Enter # of copies to be printed: "))

price = 0.0
# if copies > 0 and copies <= 99:
if 0 < copies <= 99:
  price = .30
elif 99 < copies <= 499:
  price = .28
elif 499 < copies <= 749:
  price = .27
elif 749 < copies <= 1000:
  price = .26
elif copies > 1000:
  price = .25
else:
  print("The # of copies is invalid")

print("Price per copy is: $" + str(price))
print("Total cost is: $" + str(price*copies))