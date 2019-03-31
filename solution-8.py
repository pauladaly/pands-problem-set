# Paula Daly Solution to Problem 8 March 2019
# Datetime
import datetime as dt
# Setting the display of todays date in the fomat Day, Month, Date, Year, time
today = dt.datetime.strftime(dt.datetime.now(),"%A, %B %dth, %G at %I:%M%p")
print(today)