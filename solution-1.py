# Paula Daly Solution to Problem 1 March 2019
# Getting user to input an integer
i = int(input("Please enter a positive integer: "))
# Value to work from to let user know if they did not enter a postive integer
total = 0

try:
  while i > 0:
    total = total + i
    i = i - 1
# telling user to input a differnt value as the value they entered was not a positive integer
  if i < 0:
    print("Please retry with a positive integer")
# telling user to input a positive integer after they inputted a value that was not an integer
except ValueError:
    print("Please retry with a positive integer")  

print(total)