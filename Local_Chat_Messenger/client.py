import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter your message (or 'exit' to quit): ")
        if message == 'exit':
            break
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print('Received:', data.decode('utf-8'))
