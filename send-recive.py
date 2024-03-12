import time
import random
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

link = "tcp:127.0.0.1:5762"
#link = "udp:127.0.0.1:14550"
#link = "/dev/ttyACM0"
# create a source component
my_process = utility.mavlink_connection(device=link,
                                        source_system=3,
                                        source_component=2)
my_process.wait_heartbeat()

# inform user
print("Serving as a system:", my_process.source_system, ", component:", my_process.source_component)

my_process.param_fetch_all()

# create an infinite loop
while True:

    # create the text
    text = "AI-test"

    # create STATUSTEXT message
    message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO,
                                                 text=text.encode("utf-8"))

    # send message to the GCS
    my_process.mav.send(message)
    
    m = my_process.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)
    
    print(m)
    # sleep a bit
    time.sleep(1)