import socket

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADER_SIZE]}')
            msg_len = int(msg[:HEADER_SIZE])
            new_msg = False
        full_msg += msg.decode("utf-8")
        
        if len(full_msg)-HEADER_SIZE == msg_len:
            print("Full message recieved")
            print(full_msg[HEADER_SIZE:])
            open("/home/pi/Documents/Home-Gardening-System-II--main/test_data_client.json", "w").write(full_msg[HEADER_SIZE:])
            new_msg = True
            full_msg = ''
    print(full_msg)