# Paula Daly Solution to Problem 9
# Reading Text files
with open("moby-dick.txt", "r") as f:
  for l in f.read().split("\n")[1::2]: # for loop to iterate through each line and slicing ot get every 2nd line
    print(l)