from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('', 8089)) # puerto del servidor
server.listen(1)

while True:
    # Esperando una conexión
    client, clientInfo = server.accept()

    # Información cliente
    print(clientInfo)
    data = client.recv(1024)

    print(data) # datos del cliente

    # Texto con nombre y carnet
    response = "Nombre completo: Johnston Castillo Valencia, CI: 4885794 LP"
    client.sendall(response.encode())
    client.close()
