from socket import *

# direccion del servidor
srv_addr = ("localhost", 21567)

# creando socket cliente
sockClient = socket(AF_INET, SOCK_DGRAM)

# leyendo argumentos y armando el mensaje
a, b = map(str, input("Ingrese 2 numeros enteros: ").split())
mensaje = a + ":" + b

# enviando mensaje al servidor
sockClient.sendto(mensaje.encode(), srv_addr)

# recibimos respuesta
respuesta, addr = sockClient.recvfrom(1024)
print(respuesta.decode())