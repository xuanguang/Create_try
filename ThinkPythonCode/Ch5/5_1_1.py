import time

t = time.time()
#print(time.time())

days = t // (3600*24)
years = days //365
seconds = t % (3600*24)
h = seconds // 3600
m = (seconds - h*3600) // 60
s = seconds % 60
print("Day:Year:Hour:Min:Sec\n",int(days), ":",int(years),":", int(h), ":", int(m), ":", int(s))