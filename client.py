# import bluetooth
# 
# serverMACAddress = 'DC:A6:32:B3:04:93'
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import bluetooth
import json
import time

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "/home/pi/Documents/ECEN499/Home-Gardening-System-II--main/data.json":
            with open("/home/pi/Documents/ECEN499/Home-Gardening-System-II--main/data.json", "r") as jsonyboi:
                data = jsonyboi.read()
            if data:
                sock.send(json.dumps(data).encode())#dumps incode
                print("we sent the data")

addr = 'DC:A6:32:B3:04:93'

# if len(sys.argv) < 2:
#     print("No device specified. Searching all nearby bluetooth devices for "
#           "the SampleServer service...")
# else:
# addr = sys.argv[1]
print("Searching for SampleServer on {}...".format(addr))
service_matches = []
i = 0
# search for the SampleServer service
while(len(service_matches) == 0):
    i += 1
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    service_matches = bluetooth.find_service(uuid=uuid, address=addr)
    if (i % 500 == 0):
        print("Searching for SampleServer on {}...".format(addr))
        i = 0
        time.sleep(1)

# if len(service_matches) == 0:
#     print("Couldn't find the SampleServer service.")
#     sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

observer = Observer()
observer.schedule(Handler(), '/home/pi/Documents/ECEN499/Home-Gardening-System-II--main/')
observer.start()

print("Connected.")
while True:
    new_data = sock.recv(1024)
    with open("/home/pi/Documents/ECEN499/Home-Gardening-System-II--main/test_data_2.json", "w") as fileManager:
        fileManager.write(json.loads(new_data))
        print("we have recieved data", time.time())
    #time.sleep(5)# send whenever its updated, receive everyminute
    
observer.join()
sock.close()