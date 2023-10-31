import socket
import ssl
import threading

def connect(plainToken):
    hostname = 'chat.grindr.com'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 453)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
            print(secure_sock.version())
            secure_sock.send(f"<session to='chat.grindr.com' auth_data='{plainToken}' resource='3e6f228230b9c7b3' stream_management='true' carbons='true' compress='false'>".encode())
            while True:
                msgReceived = secure_sock.recv(2048)
                if msgReceived:
                    print(msgReceived.decode())