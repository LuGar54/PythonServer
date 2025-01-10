import socket

host = "18.219.20.117"
port = 5000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

# message = input(" -> ")  # take input
message = "Salut c'est le client."

# while message.lower().strip() != 'bye':
#     client_socket.send(message.encode())  # send message
#     data = client_socket.recv(1024).decode()  # receive response

#     print('Received from server: ' + data)  # show in terminal

#     message = input(" -> ")  # again take input

client_socket.send(message.encode())  # send message
data = client_socket.recv(1024).decode()  # receive response
print('Received from server: ' + data)  # show in terminal

client_socket.close()  # close the connection