import socket
import time

message = b'01234567\n'
server_address = ('192.168.1.131',10000)
#server_address = ('192.168.1.157',10000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(server_address)
segundos = range(5)

for segundo in segundos:
    print('Envia paquete en {}'.format(5-segundo))
    time.sleep(1)

codes = range(50)
for code in codes:
    try:
        s.sendall(message)
    except:
        print('falla al enviar')
    time.sleep(0.333)
print('Closing socket')
s.close()
