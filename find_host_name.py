import socket

ip = str(input())
hostname, _, _ = socket.gethostbyaddr(ip)
print(hostname)