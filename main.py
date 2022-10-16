import time
from datetime import datetime
import PiRecord


# Initial call for the variables to use inside the loop
S = datetime.now()
CT = S.strftime('%H:%M:%S')
I = '24:01:01'
x = 0
RECschedule = {}
reclength = {}
# an infinite loop to make sure the app works around the clock
while S != I:
    # a live monitor for the recording .txt file
    # it is also a way to add the time and duration to use for recording
    # and also ignore the file errors to avoid crashes
    RECschedule = {}
    with open("/.txt") as f:   #Here you add the .txt file location
        for line in f:
            try:
                (key, val) = line.split()
            except ValueError:
                pass
            else:
                RECschedule[str(key)] = int(val)
    reclength = RECschedule
    # Adding a way to read time live to know when to start the recording
    S = datetime.now()
    CT = S.strftime('%H:%M:%S')
    time.sleep(1)
    # the if statement here is to assign the duration and start the recording
    if CT in reclength:
        rt = reclength[CT]
        PiRecord.recorde(rt)
