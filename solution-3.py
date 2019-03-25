# Paula Daly Solution to Problem 3
# Python program to print all numbers between 1,000 and 10,000 divisible by 6 but not 12
   
for i in range(1000,10000):
  if i % 6 == 0 and i % 12 != 0:
    print(i)
