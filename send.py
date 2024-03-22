import time
import random
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

link = "udp:127.0.0.1:5782"
#link = "udp:127.0.0.1:14550"
#link = "/dev/ttyACM0"
# create a source component
my_process = utility.mavlink_connection(device=link)
my_process.wait_heartbeat()

# inform user
print("Serving as a system:", my_process.source_system, ", component:", my_process.source_component)

# create an infinite loop
while True:

    # create the text
    text = "AI-zprt"

    # create STATUSTEXT message
    message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO,
                                                 text=text.encode("utf-8"))

    # send message to the GCS
    my_process.mav.send(message)
    # sleep a bit
    time.sleep(1)