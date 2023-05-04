# importando el socket
from socket import *

# Funcion que devuelve a * b con sumas sin usar operador *
def ms(a, b):
    s = 0
    for i in range(1, b + 1):
        s = s + a
    return s

addr = ("127.0.0.1", 7777)
# crear UDP socket
serverSock = socket(AF_INET, SOCK_DGRAM)

# vinculamos dirección y puerto con socket
serverSock.bind(addr)

while True:
    # recibimos información del cliente
    data, addr = serverSock.recvfrom(512)

    # decodificamos mensaje debe ser 2 números: "5 7"
    msg = data.decode()

    print(msg)

    nums = msg.split()

    # preparamos respuesta
    res = "Resultado es: " + str(ms(int(nums[0]), int(nums[1])))

    # enviando respuesta codificada a direccion de cliente
    serverSock.sendto(res.encode(), addr)
