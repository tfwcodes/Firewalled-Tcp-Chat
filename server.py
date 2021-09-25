import socket
import threading


# If you want to change it just put your public ip address
ip_address = socket.gethostname()

nickname = input("Enter your nickname: ")

clients = []
sockets = []
recv_messages = []



def firewall(connection, address):
    nickname_recv = connection.recv(1024).decode()
    connection.send(nickname.encode())

    print(f"Chating with: {address} nickname: {nickname_recv}")
    clients.append(connection)
    if len(clients) >= 100000:
        print("Someone is ddosing you, exiting...")
        exit()
    else:
        while True:
            message = input("Enter your message: ")
            
            connection.send(message.encode())
            recv_mes = f"{connection.recv(1024).decode()}"
            recv_messages.append(recv_mes)
            print(f"{nickname_recv}: {recv_mes}")

def chat():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockets.append(s)

    s.bind((ip_address, 3333))
    s.listen()
    print("Waiting for the client to connect...")
    conn, addr = s.accept()
    firewall(conn, addr)


t = threading.Thread(target=chat)
t.start()
