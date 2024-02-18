import datetime

x = datetime.datetime.now()

y = datetime.datetime.now() + datetime.timedelta(days = 10)

print((y - x).days * 24 * 60 * 60)