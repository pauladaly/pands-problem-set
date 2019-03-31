# Paula Daly Solution to Problem 7 March 2019
# Square root
# import math module 
import math
# using float to allow decimal number
num = float(input("Please enter a positive number: "))
# if user inputs a number greater than zero bringing back the approx of the square root of the inputed number
if num > 0:
    print (f"the square root of {num} is approx.")
    print (round(math.sqrt(num),1))
# if user inputs a negative number 
else:
    print(num, "is not a positive number, please try again with a postive number")