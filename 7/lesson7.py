import datetime

date_now = datetime.datetime.now()
print(f"date now = {date_now}")
delta = datetime.timedelta(days=20, hours=8, weeks=4)
print(f"delta = {delta}, type = {type(delta)}")
print(date_now+delta)
