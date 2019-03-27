# Paula Daly Solution to Problem 5
# Square root
# import math module 
import math
num = float(input("Please enter a positive number: "))
if num > 0:
    print (f"the square root of {num} is approx.")
    print (round(math.sqrt(num),1))
else:
    print(num, "is not a prime number")