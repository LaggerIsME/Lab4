import socket
import threading


host = '127.0.0.1'
port = 2022

def listen_for_msg_from_server(client):

    while True:
        msg = client.recv(2048).decode('utf-8')
        if msg == '':
            print('Сообщение пустое')
        else:
            username = msg.split(": ")[0]
            content = msg.split(": ")[1]
            print(f"[{username}] {content}")

def send_message_to_server(client):

    while True:
        msg = input()
        if(msg == ''):
            print('Оно не должно быть пустым')
            exit(0)
        else:
            client.sendall(msg.encode())

def comm_to_server(client):

    username = input('Введите прозвище: ')
    if username == '':
        print('Оно не должно быть пустым')
        exit(0)
    else:
        client.sendall(username.encode())

    threading.Thread(target = listen_for_msg_from_server, args = (client, )).start()
    send_message_to_server(client)

def main():
    
    #Сокет пользователя
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Попытка подключения
    try:
        client.connect((host, port))
        print('Вы подключены!')
    except:
        print(f'Не удалось подключиться к порту {port} и хосту {host}')

    comm_to_server(client)

if __name__ == "__main__":
    main()