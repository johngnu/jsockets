from socket import *

# Funcion para multiplicar por sumas
def multiplicar(a, b):
    sum = 0
    for _ in range(b):
        sum += a
    return sum

# Creando socket UDP
serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind(("", 21567))

while True:
    # recibimos datos e informacion del cliente
    data, addr = serverSock.recvfrom(1024)

    # decodificamos los datos del mensaje
    # el cliente debe enviar 2 numeros enteros
    mensaje = data.decode()
    a, b = map(int, mensaje.split(":"))

    respuesta = "El resultado es: " + str(multiplicar(a, b))

    # enviando respuesta al cliente
    serverSock.sendto(respuesta.encode(), addr)
