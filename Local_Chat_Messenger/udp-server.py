import socket
import os

# socket.socket関数を使用して、新しいソケットを作成します。
# AF_UNIXはUNIXドメインソケットを表し、SOCK_DGRAMはデータグラムソケットを表します。
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバが接続を待ち受けるUNIXドメインソケットのパスを指定します。
server_address = '/udp_socket_file'

try:
    # もし前回の実行でソケットファイルが残っていた場合、そのファイルを削除します。
    os.unlink(server_address)
except FileNotFoundError:
    # ファイルが存在しない場合は何もしません。
    pass

# ソケットが起動していることを表示します。
print('starting up on {}'.format(server_address))

# sockオブジェクトのbindメソッドを使って、ソケットを特定のアドレスに関連付けます。
sock.bind(server_address)

# ソケットはデータの受信を永遠に待ち続けます。
while True:
    print('\nwaiting to receive message')

    # ソケットからのデータを受信します。
    # 4096は一度に受信できる最大バイト数です。
    data, address = sock.recvfrom(4096)

    # 受信したデータのバイト数と送信元のアドレスを表示します。
    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    # 受信したデータをそのまま送信元に送り返します。
    if data:
        sent = sock.sendto(data, address)
        # 送信したバイト数と送信先のアドレスを表示します。
        print('sent {} bytes back to {}'.format(sent, address))