import os
# jsonはJSONファイルの解析と生成に使用します。
import json
  
# 'config.json'という名前のJSONファイルを開いてロードします。
# config.jsonファイルには名前付きパイプに必要な設定情報が含まれています。
config = json.load(open('config.json'))
 
# 既に同じ名前のパイプが存在する場合はそれを削除します。
# これは新しいセッションをクリーンな状態から開始するためです。
if os.path.exists(config['filepath']):
    os.remove(config['filepath'])
  
# 'os.mkfifo'は、指定したパスに名前付きパイプを作成します。
# 名前付きパイプは一方向のデータフローを持つ特殊なファイルの一種です。
# パーミッションのモードを0o600に設定しています。
# 0o600は8進数表記であり、所有者が読み書き可能であることを示しています。
os.mkfifo(config['filepath'], 0o600)
    
print("FIFO named '% s' is created successfully." % config['filepath'])
print("Type in what you would like to send to clients.")
 
# ユーザーからの入力を取得し、それを名前付きパイプに書き込みます。
# 'exit'が入力されるまでこの操作を繰り返します。
flag = True
 
while flag:
    # ユーザーからの入力を取得し、`inputstr`変数に代入します
    inputstr = input()

    if(inputstr == 'exit'):
        flag = False
    else:
        # ファイルを書き込みモードで開きます。
        # `config['filepath']` は設定ファイル内のファイルパスを指定する変数です。
        with open(config['filepath'], 'w') as f:
            # ファイルオブジェクトを`f`として参照します。
            # `with` 文のコンテキスト内では、ファイルは自動的にクローズされます。
            # 書き込み操作を行います。
            f.write(inputstr)

# プログラムの終了時に名前付きパイプを削除します。
os.remove(config['filepath'])