import socket
import time
import sys
from json import dumps

MCAST_GRP = 'FF02::1'
MCAST_PORT = 9999
MULTICAST_TTL = 2
hello_time = 2

def main():
    send()

def send():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)#, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)#socket.IPV6_MULTICAST_TTL, MULTICAST_TTL)

    #f = open("DATA.txt", "rb")
    #l = f.read(1024)
    msg = {
        "type": 'HELLO'
    }

    while True:
        
        time.sleep(hello_time)
        sock.sendto(dumps(msg).encode("utf-8"), (MCAST_GRP, MCAST_PORT))
    
    print ("mensagem enviada\n")

if __name__ == '__main__':
    main()