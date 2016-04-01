"""
birthday.py
Author: Ethan Adner
Credit: Eric Dennison
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = int(datetime.today().day)
month_name = list(month_name)

name = input("Hello, what is your name? ")
date_m = input("Hi " + name + ", what was the name of the month you were born in? ")
date_y = float(input("And what year were you born in, " + name + "? "))
date_d = float(input("And the day? "))

monthnum = int(month_name.index(date_m))
if monthnum <= 12 and monthnum >= 2:
    season="winter"
elif monthnum >=3 and monthnum <=5:
    season="spring"
elif monthnum >= 6 and monthnum <=8:
    season-"summer"
else: season="autumn"

if date_y >= 1980 and date_y <= 1989:
    age="eighties"
elif date_y >= 1990 and date_y <= 1999:
    age="nineties"
elif date_y >=2000:
    age="two thousands"
else: age="stone age" 

print("")



if (monthnum == 10) and (date_d == 31):
    print("You were born on Halloween!")
elif ((monthnum == todaymonth) and (date_d == todaydate)):
    print("Happy birthday!")
else: 
    print("{0}, you are a {1} baby of the {2}.".format(name, season, age))
