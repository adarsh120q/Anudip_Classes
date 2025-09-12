import datetime as dt
import time as tm

current_date = dt.date.today()
print(f"Today's date is: {current_date}")

my_bday = dt.date(2003, 11, 23)
print(f"My Date of Birth is: {my_bday}")

curr_hr = tm.localtime().tm_hour
curr_min = tm.localtime().tm_min
curr_sec = tm.localtime().tm_sec
print(f"Current time is- {curr_hr}:{curr_min}:{curr_sec}")