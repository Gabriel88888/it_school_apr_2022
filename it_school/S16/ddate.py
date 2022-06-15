from datetime import date, datetime, time

print(datetime.now().strftime("%H:%M:%S"))

print(datetime.now().strftime("%d/%b/%y"))

b_day = datetime(1993, 3, 4)
print(b_day.strftime("%m/%d/%Y"))
