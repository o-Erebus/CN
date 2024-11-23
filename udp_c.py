import socket

# Create a UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
message = "Hello, UDP Server!"
client.sendto(message.encode(), server_address)  # Send data
data, server = client.recvfrom(1024)  # Receive response
print(f"Response from server: {data.decode()}")
client.close()
