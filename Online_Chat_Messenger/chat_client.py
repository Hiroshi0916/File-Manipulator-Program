import asyncio

async def chat_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    # ルームを作成
    writer.write(b"create:myroom:TESTROOM.5")
    data = await reader.read(100)
    print(data.decode())

    # ルームに参加
    writer.write(b"join:myroom:")
    data = await reader.read(100)
    print(data.decode())

    # メッセージの送信
    message_content = "Hello everyone!"
    message_size = len(message_content)
    writer.write(f"message:myroom:{message_size}:{message_content}".encode())

    # クローズ
    writer.close()
    await writer.wait_closed()

asyncio.run(chat_client())
