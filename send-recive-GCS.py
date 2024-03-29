#AISOFT MAVLINK COMMUNICATION SCRIPT


import time
import random
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

link1 = "tcp:127.0.0.1:5763"
link2 = "tcp:127.0.0.1:5773"
link3 = "tcp:127.0.0.1:5783"

#link = "udp:127.0.0.1:14550"
#link = "/dev/ttyACM0"
# create a source component

dronea = utility.mavlink_connection(device=link1,
                                        source_system=3,
                                        source_component=3)
dronea.wait_heartbeat()

droneb = utility.mavlink_connection(device=link2,
                                        source_system=2,
                                        source_component=2)
droneb.wait_heartbeat()

dronec = utility.mavlink_connection(device=link3,
                                        source_system=4,
                                        source_component=4)
dronec.wait_heartbeat()

# inform user
print("drone a system:", dronea.source_system, ", component:", dronea.source_component)
print("drone b system:", droneb.source_system, ", component:", droneb.source_component)
print("drone c system:", dronec.source_system, ", component:", dronec.source_component)


dronea.param_fetch_all()
droneb.param_fetch_all()
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

    send_status("GCS_to_A"+str(random.randint(0, 100)),dronea)

    send_status("GCS_to_B",droneb)

    send_status("GCS_to_C",dronec)


    
    #m = my_process.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)
    
    print(get_status(dronea)+"\n",get_status(droneb)+"\n",get_status(dronec))
    # sleep a bit
    time.sleep(1)