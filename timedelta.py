import datetime
og=datetime.datetime.now()
print("today's date:",og)
new=og-datetime.timedelta(days=4,hours=1,minutes=12,seconds=0)
print(new)