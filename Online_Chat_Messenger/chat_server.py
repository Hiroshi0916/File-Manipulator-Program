import asyncio

BUFFER_SIZE = 100
HOST = '127.0.0.1'
TCP_PORT = 8888
UDP_PORT = 8889  # UDP用の新しいポート

# データモデルの定義
class ChatClient:
    def __init__(self, address, port, writer, extra_data=None):
        self.address = address
        self.port = port
        self.writer = writer
        # self.extra_data = extra_data

    def unique_key(self):
        return f"{self.address}:{self.port}"

class ChatRoom:
    def __init__(self, title, max_participants, host):
        self.title = title
        self.max_participants = max_participants
        self.host = host
        self.participants = {}  # <string, ChatClient>のハッシュマップ

# グローバル変数でチャットルームを保持
chat_rooms = {}  # <string, ChatRoom>のハッシュマップ

async def udp_server():
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPProtocol(), local_addr=(HOST,UDP_PORT)
    )
class UDPProtocol:
    def __init__(self):
        super().__init__()

    def connection_made(self, transport):
        self.transport = transport
    
    def datagram_received(self,data,addr):
        message = data.decode()
        if ":" not in message:
            return
        
        roomname, content = message.split(":",1)
        
        if roomname in chat_rooms:
            for _, client in chat_rooms[roomname].participants.items():
                self.transport.sendto(content.encode(), (client.address, client.port))

# クライアントからの接続を処理
async def handle_client(reader, writer):
    while True:
        try:
            data = await reader.read(BUFFER_SIZE)
            if not data:
                break
            
            message = data.decode()
            print(f"Received from client:{message}")
            
            if ":" not in message:
                continue
            cmd, roomname, content = message.split(":", 2)
            print(f"Check1: {cmd}")
            print(f"Check2: {roomname}")
            print(f"Check3: {content}")

            if cmd == "create":
                if "." not in content:
                    writer.write("Invalid format for creating a room. Make sure to use '<title>.<max_participants>' format.".encode())
                    continue

                title, max_participants = content.split(".",1)
                print(f"Check4: {title}")
                print(f"Check5: {max_participants}")

                client_address, client_port = writer.get_extra_info('peername')
                print(f"Check6: {client_address}")
                print(f"Check7: {client_port}")
                chat_rooms[roomname] = ChatRoom(title, max_participants, ChatClient(client_address, client_port,writer))  # 例: 5人まで
                print(f"Check8: {chat_rooms[roomname]}")
                writer.write(f"Room {roomname} created with title {title} and max participants {max_participants}".encode())
                print(f"Check9: Room {roomname} created with title {title} and max participants {max_participants}".encode())
                # loop = asyncio.get_event_loop()
                # loop.create_task(udp_server())


            elif cmd == "join":
                print(f"Check10: {cmd}")
                client_address, client_port = writer.get_extra_info('peername')
                client_key = f"{client_address}:{client_port}"

                already_joined = any(client_key in room.participants for room in chat_rooms.values())
                if already_joined:
                    writer.write("You're already in a room. Leave in before joining another.".encode())
                    continue

                if roomname in chat_rooms:
                    if len(chat_rooms[roomname].participants) >= chat_rooms[roomname].max_participants:
                        writer.write(f"Room {roomname} is full".encode())
                    else:
                        client = ChatClient(client_address, client_port, writer)
                        chat_rooms[roomname].participants[client.unique_key()] = client
                        writer.write(f"Joined room {roomname}".encode())
                else:
                    writer.write(f"Room {roomname} does not exist".encode())

            elif cmd == "message":
                if content.count(":") != 1:
                    writer.write("Invalid format for sending a message. Make sure to use '<room_size>:<actual_message>' format.".encode())
                    continue
            
            room_size_str, actual_message = content.split(":", 1)
            room_size = int(room_size_str)

            if len(actual_message) != int(room_size):
                writer.write("Invalid message size.".encode())
                continue

            if roomname in chat_rooms:
                client_address, client_port = writer.get_extra_info('peername')
                client_key = f"{client_address}:{client_port}"

                if client_key not in chat_rooms[roomname].participants:
                    writer.write("You're not a participant in this room.".encode())
                    continue

            # この部屋に参加しているすべてのクライアントにメッセージをブロードキャスト
                for client_key, client in chat_rooms[roomname].participants.items():
                    if client_key != f"{client_address}:{client_port}":
                        try:
                            client.writer.write(f"{client_address}: {actual_message}\n".encode())
                            await client.writer.drain()
                        except:
                            print(f"Error while broadcasting: {str(e)}")
                            # pass  # 例外処理: 接続が切れたクライアントを取り扱います
                            break

                    # if client_key != f"{writer.get_extra_info('peername')[0]}:{writer.get_extra_info('peername')[1]}":
                    #     writer.write(f"{content}\n".encode())
                    #     await client.writer.drain()
        except Exception as e:
             writer.write(f"error:An unexpected error occurred: {str(e)}".encode())
        continue

    writer.close()
    await writer.wait_closed()

# メインサーバロジック
async def main():
    await udp_server()
    server = await asyncio.start_server(handle_client, HOST, TCP_PORT)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

# サーバーを実行
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
