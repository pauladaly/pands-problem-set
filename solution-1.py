# Paula Daly Solution to Problem 1
i = int(input("Please enter a positive integer: "))
total = 0
try:
  while i > 0:
    total = total + i
    i = i - 1

  if i < 0:
    print("Please retry with a positive integer")

except ValueError:
    print("Please retry with a positive integer")  

print(total)