import socket

HOST = '127.0.0.1'  # Ip as a Global Variable
PORT = 12345        # Using port as any number allowed


def client_fun(conn, addr):      # Client Function
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break
        print(f"Received from {addr}: {data}")  # Taking data from the Address

        checked_char = data[0]  # splitting first character to make apply the 3 conditions on it
        remain_string = data[1:]  # remaining string would be the output
        if checked_char == 'A':
            resulted_string = ''.join(sorted(remain_string))  # sort the string if first char A
        elif checked_char == 'C':
            resulted_string = remain_string.upper()  # capitalize the string if first char C
        elif checked_char == 'D':
            resulted_string = ''.join(sorted(remain_string, reverse=True))  # reverse the string if first char D
        else:
            resulted_string = data  # if none of input strings first char is A or C ,D Do Nothing

        conn.sendall(resulted_string.encode())
        print(f"Sent to {addr}: {resulted_string}")

    conn.close()
    print(f"Connection from {addr} closed")


def server():               # running server function
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT)) # IP -- PORT
        s.listen()
        print(f"Server listening on port {PORT}")

        while True:
            conn, addr = s.accept()
            client_fun(conn, addr)


if __name__ == '__main__':
    server()
