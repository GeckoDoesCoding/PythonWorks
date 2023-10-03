import socket
#works 
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1221))

print("Roll and Pitch Values are: ")

while True:
    msg1 =s.recv(1024)
    print(msg1.decode("utf-8"))

    msg2 =s.recv(1024)
    print(msg2.decode("utf-8") )

#a = int(msg1.decode("utf-8")) + int(msg2.decode("utf-8"))
#print(a)