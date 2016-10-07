import os
from datetime import datetime
import time
duration=int(raw_input("How many minutes? : "))
st = raw_input("Message : ")
time.sleep(((duration*60)-10))
for i in range(10,0,-1):
	time.sleep(1)
	os.system('say "'+str(i)+'"')
os.system('say "'+str(st)+'"')
print "Finish at : "+(str(datetime.now().time())).split(".")[0]

