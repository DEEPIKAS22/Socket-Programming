import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect(("127.0.0.1",5000))
s.send(b"Connected to client")
print(s.recv(1024).decode()) 
print("Type a message\n\n")
i=1
while i==1:
    c1=input("Your Message:")
    s.send(c1.encode())
    if c1=='bye':
        s.send(b"Connection is terminated cli2")   
        print(s.recv(1024).decode()) 
        i=0
    else:
        m=s.recv(1024).decode()
        print("\t\t\t\t\t\tFrom User:",m)
        if m=='bye':
            s.send(b"Connection is terminated cli2")   
            print(s.recv(1024).decode())
            i=0



