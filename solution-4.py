# Paula Daly Solution to Problem 4 March 2019
# Collatz - particular sequence always reaches 1

# Defining the function 
def collatz(number):
    # looping through and if number found is even divide it by 2
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    # looping through and if the number is odd multiply it by 3 and add 1
    elif number % 2 != 0:
        result = 3 * number + 1
        print(result)
        return result

try:
    # ask the user to enter a number
    n = input("Enter number: ")
    # running the function
    while n != 1:
        n = collatz(int(n))
# what to do if the user inputs a negative integer      
except ValueError:
    print('Please enter a positive integer')