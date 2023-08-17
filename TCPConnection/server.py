import socket
import os
from pathlib import Path

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = '0.0.0.0'
server_port = 9001

# 現在の作業ディレクトリを作成します
dpath = 'temp'
if not os.path.exists(dpath):
   os.makedirs(dpath)

print('Starting up on {} port {}'.format(server_address, server_port))

# サーバアドレスとポートを指定してバインドするためのタプルを渡します
sock.bind((server_address, server_port))

sock.listen(1)

while True:
   # TCP接続は、まず接続を受け入れなければなりません。これにより、サーバとクライアントの間でハンドシェイクが設定されます。
   connection, client_address = sock.accept()
   try:
      print('connection from', client_address)
      header = connection.recv(8)

      filename_length = int.from_bytes(header[:1], "big")
      json_length = int.from_bytes(header[1:3], "big")
      data_length = int.from_bytes(header[4:8], "big")
      stream_rate = 4096

      print('Received header from client. Byte lengths: Title length {}, JSON length {}, Data Length {}'.format(filename_length, json_length,data_length))

      filename = connection.recv(filename_length).decode('utf-8')

      print('Filename: {}'.format(filename))

      if json_length != 0:
         raise Exception('JSON data is not currently supported.')
      
      if data_length == 0:
         raise Exception('No data to read from client.')
      
      # w+は終了しない場合はファイルを作成し、そうでない場合はデータを切り捨てます
      with open(os.path.join(dpath, filename),'wb+') as f:
         # すべてのデータの読み書きが終了するまで、クライアントから読み込まれます
         while data_length > 0:
            data = connection.recv(data_length if data_length <= stream_rate else stream_rate)
            f.write(data)
            print('recieved {} bytes'.format(len(data)))
            data_length -= len(data)
            print(data_length)
      
      print('Finished downloading the file from client.')
      
   except Exception as e:
      print('Error: ' + str(e))

   finally:
      print("Closing current connection")
      connection.close()