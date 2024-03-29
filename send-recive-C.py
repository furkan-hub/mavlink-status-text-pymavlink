#AISOFT MAVLINK COMMUNICATION SCRIPT


import time
import random
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

link = "tcp:127.0.0.1:5782"
#link = "udp:127.0.0.1:14550"
#link = "/dev/ttyACM0"
# create a source component

dronec = utility.mavlink_connection(device=link,
                                        source_system=4,
                                        source_component=4)
dronec.wait_heartbeat()

# inform user
print("Serving as a system:", dronec.source_system, ", component:", dronec.source_component)

dronec.param_fetch_all()


def send_status(data,drone):
    text = data #gonderilecek mesaj

    # create STATUSTEXT message
    message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO,
                                                 text=text.encode("utf-8"))

    # send message to the GCS
    drone.mav.send(message)
    

def get_status(drone):
    m = drone.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)#mesajı alma objesi
    
    if m is not None:  # m'nin None olup olmadığını kontrol et
        desired_data = m.text
    else:
        desired_data = "No data received"  # veya uygun bir hata mesajı / varsayılan değer
    
    return desired_data  # mesajı döndür


# create an infinite loop
while True:

    send_status("Drone_C_To_GCS",dronec)
    
    
    #m = my_process.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)
    
    print(get_status(dronec))
    # sleep a bit
    time.sleep(1)