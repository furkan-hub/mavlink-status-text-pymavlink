from dronekit import connect, VehicleMode
from pymavlink import mavutil
import time

# Bağlantı ayarları
connection_string = 'udp:127.0.0.1:5773'  # ArduPilot'un bağlantı adresi
vehicle = connect(connection_string, wait_ready=False)

while True:
    time.sleep(1)
    print(vehicle.location.global_frame.alt)