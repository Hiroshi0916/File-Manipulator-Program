import socket
import sys
import os

# サーバに送信するヘッダフォーマー。プロトコルの情報を64ビットで返します
def protocol_header(filename_length, json_length, data_length):
   return filename_length.to_bytes(1, "big") + json_length.to_bytes(3,"big") + data_length.to_bytes(4,"big")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# サーバが待ち受けているポートにソケットを接続します
server_address = input("Type in the server's address to connect to: ")
server_port = 9001

print('connecting to {}'.format(server_address, server_port))

try:
   # 接続後、サーバとクライアントが相互に読み書きができるようになります 
   sock.connect((server_address, server_port))
except socket.error as err:
   print(err)
   sys.exit(1)

try:
   # ファイルを送信する場合は、テキストファイルで2GB以下に制限してください
   filepath = input('Type in a file to upload: ')

   # バイナリモードでファイルを読み込む
   with open(filepath, 'rb') as f:
      # ファイルの末尾に移動し、tellは開いているファイルの現在位置を返します。ファイルのサイズを取得するために使用します
      f.seek(0, os.SEEK_END)
      filesize = f.tell()
      f.seek(0,0)

      if filesize > pow(2,32):
         raise Exception('File must be below 2GB.')

      filename = os.path.basename(f.name)

      # ファイル名からビット数
      filename_bits = filename.encode('utf-8')

      header = protocol_header(len(filename_bits), 0, filesize)

      # ヘッダの送信
      sock.send(header)

      # ファイル名の送信
      sock.send(filename_bits)

      # 一度に4096バイト（4096ビット）ずつ読み出し、送信することにより、ファイルを送信します。Readは読み込んだビットを返します
      data = f.read(4096)
      while data:
         print("Sending...")
         sock.send(data)
         data = f.read(4096)

finally:
   print('closing socket')
   sock.close()