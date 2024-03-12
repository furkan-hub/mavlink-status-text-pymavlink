"""
    If you have a companion computer on your vehicle, you can send a status text
    message from the companion computer to the GCS using the MAVLink protocol to
    inform the user of the status of the process running on the companion computer.

    This is useful for debugging and for creating and sending messages to the GCS
    that are not part of the standard MAVLink protocol. And also the companion
    computer uses the MAVLink protocol and underlying infrastructure.

    This example assumes that you have a companion computer on your vehicle and
    that you have a UDP connection between the companion computer and the GCS.

    Device string for UDP connection: "udpout:127.0.0.1:14560" means that the
    companion computer acts as a source component (like the autopilot on the
    MAVLink connection) and sends messages to the GCS on the local machine.

    At the ardu-sim.sh, replace the "--out 127.0.0.1:14560" with "--master 127.0.0.1:14560"

    https://mavlink.io/en/messages/common.html#STATUSTEXT
"""

import time
import random
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

link = "tcp:127.0.0.1:5762"
#link = "udp:127.0.0.1:14550"
#link = "/dev/ttyACM0"
# create a source component
my_process = utility.mavlink_connection(device=link,
                                        source_system=2,
                                        source_component=2)
my_process.wait_heartbeat()

# inform user
print("Serving as a system:", my_process.source_system, ", component:", my_process.source_component)

# create an infinite loop
while True:

    # create the text
    text = "AI-test"

    # create STATUSTEXT message
    message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO,
                                                 text=text.encode("utf-8"))

    # send message to the GCS
    my_process.mav.send(message)
    # sleep a bit
    time.sleep(1)