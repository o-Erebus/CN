import socket

# Create a TCP server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))  # Bind to localhost and port 12345
server.listen(1)
print("TCP Server listening on port 12345...")

while True:
    conn, addr = server.accept()
    print(f"Connection established with {addr}")
    data = conn.recv(1024).decode()
    if data:
        print(f"Received from client: {data}")
        conn.send(f"Echo: {data}".encode())
    conn.close()
