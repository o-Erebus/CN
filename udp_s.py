import socket

# Create a UDP server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))  # Bind to localhost and port 12345
print("UDP Server listening on port 12345...")

while True:
    data, addr = server.recvfrom(1024)  # Receive data from client
    print(f"Received from {addr}: {data.decode()}")
    server.sendto(f"Echo: {data.decode()}".encode(), addr)  # Send response
