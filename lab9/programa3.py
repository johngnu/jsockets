import socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('localhost', 80))
misock.send('GET http://localhost/index.html HTTP/1.0\n\n'.encode("utf-8"))
while True:
    datos = misock.recv(512)
    if ( len(datos) < 1 ) :
        break
    print(datos.decode('utf-8'))
misock.close()
