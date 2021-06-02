
#!/usr/bin/env python3
"""PyBluez simple example rfcomm-server.py
Simple demonstration of a server application that uses RFCOMM sockets.
Author: Albert Huang <albert@csail.mit.edu>
$Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
"""

import bluetooth
import json
import time
import os
from _thread import *
import threading

print_lock = threading.Lock()

def receiveData(c):
    print("in recieve data")
    while True:
        data = c.recv(1024)
        data = json.loads(data.decode())
        if not data:
            break
        print("Received", data)
        with open("/home/pi/recvData.json","w") as fileWriter:
            fileWriter.write(data)

def sendData(c):
    print("in send data")
    while True:
        with open("/home/pi/sendData.json","r") as fileHandler:
            sendData = fileHandler.read()
        sendData = json.dumps(sendData).encode()
        c.send(sendData)
        time.sleep(5)

os.system("sudo hciconfig hci0 piscan")

client_MAC = 'E4:5F:01:0F:CA:BD'
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(('', 1))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print_lock.acquire()
print("Accepted connection from", client_info)
os.system("sudo hciconfig hci0 noscan")
try:
    start_new_thread(sendData,(client_sock,))
    start_new_thread(receiveData,(client_sock,))
    while True:
        pass
except OSError:
    pass

print("Disconnected.")

client_sock.close()
server_sock.close()
print("All done.")