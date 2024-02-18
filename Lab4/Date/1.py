import datetime

x = datetime.datetime.now()
y = datetime.datetime.now() - datetime.timedelta(5)
print("5 days before: ", y)
print("Today: ", x)