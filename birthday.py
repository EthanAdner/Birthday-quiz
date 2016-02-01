"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
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
from datetime import datetime as DATE
from calendar import month_name as MONTH


name=str(input("What is your name? "))
born_m=str(input("During what month were you born? "))
born_md=born_m.lower()
born_y=str(input("What year were you born in? "))
born_d=str(input("What day were you born? "))

if(born_d==datetime.today().day):
    if(born_md==datetime.today().month):
        print("Happy birthday")

