import socket

HOST = '127.0.0.1'  # IP address of the server
PORT = 12345     # Port number used by the server


def client_input():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:             # taking input till connection still on
            message = input("Please enter a message: \n")
            if not message:
                break
            client.sendall(message.encode())
            response = client.recv(1024).decode().strip()
            print(f"Received from server: {response}")


if __name__ == '__main__':
    client_input()
