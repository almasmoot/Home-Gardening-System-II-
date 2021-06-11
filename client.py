import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#import bluetooth
import json
import time

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "C:\\Users\\max58\\Home-Gardening-System-II-\\data.json":
            with open("C:\\Users\\max58\\Home-Gardening-System-II-\\data.json", "r") as jsonyboi:
                data = jsonyboi.read()
            if data:
                print(data)
                #sock.send(json.dumps(data).encode())#dumps incode

class ClientBluetooth():
    def connect(self):
        addr = 'DC:A6:32:B3:04:93'

        print("Searching for SampleServer on {}...".format(addr))
        service_matches = []
        i = 0
        # search for the SampleServer service
        while(len(service_matches) == 0):
            i += 1
            uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
            #service_matches = bluetooth.find_service(uuid=uuid, address=addr)
            service_matches.append({"port": 0, "name": "maxwell", "host": "windows"})
            if (i % 500 == 0):
                print("Searching for SampleServer on {}...".format(addr))
                i = 0
                time.sleep(1)

        first_match = service_matches[0]
        port = first_match["port"]
        name = first_match["name"]
        host = first_match["host"]

        print("Connecting to \"{}\" on {}".format(name, host))

        # Create the client socket
        #sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        #sock.connect((host, port))
        sock = ""
        return sock


    def send_and_recieve_data(self):
        
        sock = self.connect()

        observer = Observer()
        # /home/pi/Documents/ECEN499/Home-Gardening-System-II--main/
        observer.schedule(Handler(), 'C:\\Users\\max58\\Home-Gardening-System-II-')
        observer.start()

        print("Connected.")
        while True:
            #new_data = sock.recv(1024)
            print("heehoo")
            time.sleep(5)
            #with open("/home/pi/Documents/ECEN499/Home-Gardening-System-II--main/test_data_2.json", "w") as fileManager:
                #fileManager.write(json.loads(new_data))
                # send whenever its updated, receive everyminute
    
        observer.join()
        #sock.close()