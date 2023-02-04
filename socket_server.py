import socket
import time
import signal
import sys

host = "localhost"
port = 12345
bufsize = 512

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

def sig_handler(signal, frame):
    print("close")
    sock.close()
    sys.exit(0)

# Ctrl+C
signal.signal(signal.SIGINT, sig_handler)

k = 0
print("Recieve #: Forward")
while True:
    data, addr = sock.recvfrom(bufsize)
    data_time = str(time.time())
    forward = float(data_time) - float(data)
    print(f'Recieve {k}: {"%.8f" % forward}')
    sock.sendto(data_time.encode('utf-8'), addr)
    k += 1
