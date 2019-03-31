# Paula Daly Solution to Problem 3 March 2019
# Python program to print all numbers between 1,000 and 10,000 divisible by 6 but not 12

# inputing the range the program is to work with   
for i in range(1000,10000):
  # Getting the program to retun the values returned from the range set up that are divisible by 6 but not divisible by 12
  if i % 6 == 0 and i % 12 != 0:
    # Showing the results of the program
    print(i)
