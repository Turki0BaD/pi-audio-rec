import time
from datetime import datetime

RECschedule = {}
with open("RECTIME.txt") as f:
    for line in f:
        (key, val) = line.split()
        RECschedule[str(key)] = int(val)

S = datetime.now()
CT = S.strftime('%H:%M:%S')

reclength = RECschedule
