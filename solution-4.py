# Paula Daly Solution to Problem 4
# Collatz

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 != 0:
        result = 3 * number + 1
        print(result)
        return result

try:
    n = input("Enter number: ")
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print('Please enter a positive integer')