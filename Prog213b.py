#0	-	99	$5.95
#100	-	199	$5.75
#200	-	299	$5.40
#300 	&	 up	$5.15

with open("Langdat/prog213b.txt", 'r') as f:
  num = int(f.readline())
  Price = 0.00
  Amount = 0.00
  if num >= 0 and num <= 99:
    Price = 5.95
  elif num >= 100 and num <= 199:
    Price = 5.75
  elif num >= 200 and num <= 299:
    Price = 5.40
  elif num >= 300:
    Price = 5.15

Amount = num * Price
print("Quantity:", num, "Price per item:", Price, "Total Amount:", Amount)