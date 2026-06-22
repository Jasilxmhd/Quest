
import socket

server = socket.socket()

host = '127.0.0.1'
port = 2004

server.bind((host,port))

server.listen()

connection, addressss = server.accept()

print("connection from : ",str(addressss))

while True:
    data = connection.recv(1024).decode()

    if not data:
        break

    data = str(data).upper()
    print(f'from cilent :{str(data)}')
    typing = input("Type message : ")
    connection.send(data.encode())


connection.close()
