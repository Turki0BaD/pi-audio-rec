import time
from datetime import datetime
import PiRecord


S = datetime.now()
CT = S.strftime('%H:%M:%S')
I = '24:01:01'
x = 0
RECschedule = {}
reclength = {}
while S != I:
    RECschedule = {}
    with open("recpi/RECTIME.txt") as f:
        for line in f:
            (key, val) = line.split()
            RECschedule[str(key)] = int(val)
    reclength = RECschedule
    S = datetime.now()
    CT = S.strftime('%H:%M:%S')
    time.sleep(1)
    if CT in reclength:
        rt = reclength[CT]
        PiRecord.recorde(rt)
