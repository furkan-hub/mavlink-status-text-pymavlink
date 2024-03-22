#AISOFT MAVLINK COMMUNICATION SCRIPT


import time
from pymavlink import mavutil
import pymavlink.dialects.v20.all as dialect

link = "udp:127.0.0.1:5762"


# Connect to Pixhawk over serial port
master = mavutil.mavlink_connection(device=link)
master.wait_heartbeat()
print("ok")

master.param_fetch_all()
 
while True:
    m = master.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)
    if m:
        print("system: ",m.get_srcSystem())
        print(m)

    # if m is None:
    #             break