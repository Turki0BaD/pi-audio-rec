import time
from datetime import datetime

S = datetime.now()
CT = S.strftime("%H:%M:%S")
rectime = {"11:07:00", "11:08:00", "10:09:00", "10:10:00", "10:11:00"}
reclength = {
    "11:07:00": 30,
    "11:08:00": 15,
    "10:09:00": 30,
    "10:10:00": 40,
    "10:11:00": 55,
}
