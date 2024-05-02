import socket

HOST ="127.0.0.1"
PORT=65432
PACKET=1000
def send_packet():
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
        for _ in range(PACKET):
            s.sendto(b"hello ",(HOST,PORT))
if __name__ == "__main__":
    send_packet()



              