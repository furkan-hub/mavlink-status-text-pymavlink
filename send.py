#AISOFT MAVLINK COMMUNICATION SCRIPT


import time
import random
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

link = "udp:127.0.0.1:5782"
#link = "udp:127.0.0.1:14550"
#link = "/dev/ttyACM0"

# create a source component
my_process = utility.mavlink_connection(device=link)# bağlantı adresi 
my_process.wait_heartbeat()#heartbeat bekle

# inform user
print("Serving as a system:", my_process.source_system, ", component:", my_process.source_component)# bilgilendirme çıktısı

# create an infinite loop
while True:

    # create the text
    text = "AI-test2"#string

    # create STATUSTEXT message
    message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO,text=text.encode("utf-8")) #status text message

    # send message to the GCS
    my_process.mav.send(message) #mesajı gönder

    time.sleep(1)# bekle