import socket
import threading

nickname = input("Enter your nickname: ")

# If you want to change it just put your public ip address
ip_address = socket.gethostname()

def chat():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, 3333))

    s.send(nickname.encode())
    nickname_recv = s.recv(1024).decode()
    print(f"Chating with {nickname_recv}")

    while True:
        print(f"{nickname_recv}: {s.recv(1024).decode()}")
        message = input("Enter your message: ")
        s.send(message.encode())

t = threading.Thread(target=chat)
t.start(chat)