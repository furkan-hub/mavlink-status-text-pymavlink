import time
from pymavlink import mavutil
import pymavlink.dialects.v20.all as dialect

link = "udp:127.0.0.1:5783"


# Connect to Pixhawk over serial port
master = mavutil.mavlink_connection(device=link,
                                     source_system=2,
                                     source_component=3)
master.wait_heartbeat()
print("ok")

master.param_fetch_all()
 
while True:
    m = master.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)
    print(m)
    # if m is None:
    #             break