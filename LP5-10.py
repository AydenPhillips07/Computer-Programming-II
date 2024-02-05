import math
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Second Number: "))
#ans = math.gcd(num1, num2) easy way
#print("The GCD is: ", ans)
while (num1 > 0 and num2 > 0):
  temp = num1 % num2
  num1 = num2
  num2 = temp

print("The GCD is: ", num1)
  
