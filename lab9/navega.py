import socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('localhost', 80))
misock.send('GET http://locahost/images.jpeg HTTP/1.0\n\n'.encode("utf-8"))
cont=0
imagen=""
while (True):
    datos = misock.recv(234)
    if ( len(datos) < 1 ) :
        break
    imagen=imagen+datos
u=imagen.find("\r\n\r\n")
nueva=imagen[u+4:]   
file=open("descar.jpeg","wb")
file.write(nueva)
misock.close()
print(file)
