import socket
from faker import Faker

fake = Faker()

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server started. Waiting for connection...')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print('Received:', data)
            
            # Using Faker to generate a fake response
            response = fake.sentence()
            print('Sending:', response)
            conn.sendall(response.encode('utf-8'))
