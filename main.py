import time
from datetime import datetime
import PiRecord
import PiTimeControl

S = datetime.now()
CT = S.strftime("%H:%M:%S")
I = "24:01:01"
x = 0


while S != I:
    S = datetime.now()
    CT = S.strftime("%H:%M:%S")
    time.sleep(1)
    if CT in PiTimeControl.rectime:
        rt = PiTimeControl.reclength[CT]
        PiRecord.recorde(rt)
