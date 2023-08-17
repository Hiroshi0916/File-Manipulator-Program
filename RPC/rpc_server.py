import socket
import json
import math

HOST = '127.0.0.1'
PORT = 65432

# RPC関数
def floor(x: float) -> int:
    return math.floor(x)

def nroot(n: int, x: int) -> float:
    return x ** (1/n)

def reverse(s: str) -> str:
    return s[::-1]

def validAnagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)

def sort(strArr: list) -> list:
    return sorted(strArr)

# サーバ起動
def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print("Server started. Waiting for connections...")

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                request = json.loads(data)
                
                method = request.get("method")
                params = request.get("params")
                
                # エラーハンドリングと関数実行
                try:
                    if method == "floor":
                        result = floor(*params)
                    elif method == "nroot":
                        result = nroot(*params)
                    elif method == "reverse":
                        result = reverse(*params)
                    elif method == "validAnagram":
                        result = validAnagram(*params)
                    elif method == "sort":
                        result = sort(*params)
                    else:
                        raise ValueError(f"Method {method} not found")
                    
                    response = {
                        "result": result,
                        "result_type": type(result).__name__,
                        "id": request.get("id")
                    }
                except Exception as e:
                    response = {
                        "error": str(e),
                        "id": request.get("id")
                    }

                conn.sendall(json.dumps(response).encode('utf-8'))

if __name__ == "__main__":
    run_server()
