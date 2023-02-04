import socket
import time
import signal
import sys

host = "localhost"
port = 12345
bufsize = 512

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sig_handler(signal, frame):
    print("close")
    sock.close()
    sys.exit(0)

# Ctrl+C
signal.signal(signal.SIGINT, sig_handler)

k = 0
print("[   ], RTT(Total),    Forward,   Backward")
while True:
    start_time = str(time.time())
    sock.sendto(start_time.encode('utf-8'), (socket.gethostbyname(host), port))
    data_time, addr = sock.recvfrom(bufsize)
    end_time = str(time.time())

    forward = float(data_time) - float(start_time)
    backward = float(end_time) - float(data_time)
    total = float(end_time) - float(start_time)
    print(f'[{"%3d" % k}], {"%.8f" % total}, {"%.8f" % forward}, {"%.8f" % backward}')

    time.sleep(2)
    k += 1
