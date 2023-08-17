import asyncio

TCP_PORT = 8888
UDP_PORT = 8889
BUFFER_SIZE = 100

class UDPClientProtocol:
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        print("Received:", data.decode())

async def udp_client():
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPClientProtocol(),
        local_addr=('127.0.0.1', UDP_PORT)
    )

async def chat_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', TCP_PORT)
    
    # Start UDP client to listen for messages
    await udp_client()

    # Create room
    writer.write(b"create:myroom:This is a test room.5")  # Assuming max 5 participants
    data = await reader.read(BUFFER_SIZE)
    print(data.decode())

    # Join room
    writer.write(b"join:myroom:")
    data = await reader.read(BUFFER_SIZE)
    print(data.decode())

    # Send message
    message = "Hello everyone!"
    formatted_message = f"{len(message)}:{message}"
    writer.write(f"message:myroom:{formatted_message}".encode())
    data = await reader.read(BUFFER_SIZE)
    print(data.decode())

    # Close connection
    writer.close()
    await writer.wait_closed()

asyncio.run(chat_client())
