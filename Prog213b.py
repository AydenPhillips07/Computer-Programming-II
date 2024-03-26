#0	-	99	$5.95
#100	-	199	$5.75
#200	-	299	$5.40
#300 	&	 up	$5.15

Quant = int(input("Enter Quantity: "))
def main():
  Price = 0.00
  Amount = 0.00
  if Quant >= 0 and Quant <= 99:
    Price = 5.95
  elif Quant >= 100 and Quant <= 199:
    Price = 5.75
  elif Quant >= 200 and Quant <= 299:
    Price = 5.40
  elif Quant >= 300:
    Price = 5.15

  Amount = Quant * Price
  print("Quantity:", Quant, "Price per item:", Price, "Total Amount:", Amount)