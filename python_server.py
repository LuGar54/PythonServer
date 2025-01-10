import socket
import urllib.request

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print(external_ip)

host = socket.gethostname()

ip_address = socket.gethostbyname(host)

print(host)
print(ip_address)

#Le port du serveur doit être au-dessus de 1024, car les premiers sont réservés pour des utilités précises (genre 666 pour DOOM)
port = 5000


server_socket = socket.socket()

server_socket.bind((host, port))

server_socket.listen(2)

conn, address = server_socket.accept()

print("Nouvelle connexion de : " + str(address))
while True:
    #Ici on reçoit des données envoyées par le client
    data = conn.recv(1024).decode()
    
    if not data:
        break
    
    print("from connected user: " + str(data))
    data = "Bonjour c'est Ludo."
    conn.send(data.encode())

conn.close()