import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(("127.0.0.1",5000))
s.listen(5)
c,a1=s.accept()
c.send(b"Connected to server from client1")
print(c.recv(1024).decode())
c2,a2=s.accept()
c2.send(b"Connected to server from client2")
print(c2.recv(1024).decode())
i=1
while i==1:
    m=c.recv(1024).decode()
    if m=='bye':
        print("\t\t\t\t\t\tFrom User1:",m)
        c.send(b"Connection is terminated serverwith user1")   
        print(c.recv(1024).decode())  
        i=0
    else:
        print("\t\t\t\t\t\tFrom User1:",m)
        c1=input("Your Message for user1:")
        c.send(c1.encode())
        if c1=='bye':
            c.send(b"Connection is terminated serverwith user1")   
            print(c.recv(1024).decode())  
            i=0
    n=c2.recv(1024).decode()
    if n=='bye':
        print("\t\t\t\t\t\tFrom User2:",n)
        c2.send(b"Connection is terminated ser with user2")   
        print(c2.recv(1024).decode())  

        i=0
    else:
        print("\t\t\t\t\t\tFrom User2:",n)
        p=input("Your Message for user2:")
        c2.send(p.encode())
        if p=='bye':
            c2.send(b"Connection is terminated ser with user2")   
            print(c2.recv(1024).decode())
            i=0




