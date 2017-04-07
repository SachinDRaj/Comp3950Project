# Comp3950Project

https://github.com/drvinceknight/Simulating_Queues/blob/master/graphicalMM1.py

https://www.tutorialspoint.com/python/time_strptime.htm


http://stackoverflow.com/questions/1750644/how-to-use-python-to-calculate-time
from datetime import datetime

# Parse the time strings
t1 = datetime.strptime('01:12','%H:%M')
t2 = datetime.strptime('18:59','%H:%M')

# Do the math, the result is a timedelta object
delta = (t2 - t1) / 12
print(delta.seconds)
