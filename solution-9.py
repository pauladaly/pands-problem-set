# Paula Daly Solution to Problem 9
# Reading Text files
# Command line argument

import sys
if len(sys.argv) == 2:
  with open(sys.argv[1], "r") as f:
    for l in f.read().split("\n")[1::2]: # for loop to iterate through each line and slicing ot get every 2nd line
      print(l)
else:
  print("Please include txt file name moby-dick.txt in command line")
