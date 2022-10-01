import socket
import threading

host = '127.0.0.1'
port = 2022
def main():
    #Сокет пользователя
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Попытка подключения
    try:
        client.connect((host, port))
        print('Вы подключены!')
    except:
        print(f'Не удалось подключиться к порту {port} и хосту {host}')
if __name__ == "__main__":
    main()