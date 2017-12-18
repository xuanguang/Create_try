import time

t = time.time()
#print(time.time())

pastDays = t // (3600*24)
# years = pastDays
# //365       # wrong here! because not all the years include 365 pastDays
#!!!
secondsInlastDay = t % (3600*24)
h = secondsInlastDay // 3600
# m = (secondsInlastDay - h*3600) // 60
secondsInlastHour = secondsInlastDay % 3600
m = secondsInlastHour // 60
s = secondsInlastHour % 60
# print("Day:Year:Hour:Min:Sec\n",int(pastDays), ":", int(h), ":", int(m), ":", int(s))
print("Past days (since 1 January 1970): {0}\nHour: {1}\nMin: {2}\nSec: {3}\n".format(int(pastDays), int(h), int(m), int(s)))
