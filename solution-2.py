# Paula Daly Solution to Problem 2 March 2019
# Adding datetime module 

import datetime
# As the numbering of days of the week start from 0-6 telling the program that the 2nd and 4th day of the week start with a T
if datetime.datetime.today().weekday() == 1:
  print("Yes - today begins with a T.")
elif datetime.datetime.today().weekday() == 3:
  print("Yes - today begins with a T.")
# If at the time the program is ran and the day is either 0,2,4,5,6 tell the user the day does not begin with T  
else:
  print("No - today does not begin with a T.")