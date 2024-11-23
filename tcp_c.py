import socket

# Create a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))  # Connect to the server
message = "Hello, TCP Server!"
client.send(message.encode())  # Send data
response = client.recv(1024).decode()  # Receive response
print(f"Response from server: {response}")
client.close()
