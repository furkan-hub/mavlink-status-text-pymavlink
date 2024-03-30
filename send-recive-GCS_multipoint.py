#AISOFT MAVLINK COMMUNICATION SCRIPT

import time
import random
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

#bağlantı objesi
dronea = utility.mavlink_connection(device="/dev/ttyUSB0",baud=115200,
                                        source_system=3,
                                        source_component=3)
dronea.wait_heartbeat()

print("drone a system:", dronea.source_system, ", component:", dronea.source_component)

#parametreleri bi tur al
dronea.param_fetch_all()


def send_status(data,drone,id):
    text = data #gonderilecek mesaj

    # create STATUSTEXT message
    message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO,
                                                 text=text.encode("utf-8"))
    
    message.target_system = id
    # send message to the GCS
    drone.mav.send(message)
    

def get_status(drone):
    m = drone.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)#mesajı alma objesi
    
    if m is not None:  # m'nin None olup olmadığını kontrol et
        desired_data = m.text
    else:
        desired_data = "No data received"  # veya uygun bir hata mesajı / varsayılan değer
    
    return desired_data  # mesajı döndürd



# create an infinite loop
while True:

    send_status("GCS_to_A",dronea,1)
    send_status("GCS_to_B",dronea,2)


    #m = my_process.recv_match(type = "STATUSTEXT", blocking = True, timeout = 1)
    
    print(get_status(dronea)+"\n")
    # sleep a bit
    time.sleep(1)