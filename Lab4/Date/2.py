import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow ", tomorrow)