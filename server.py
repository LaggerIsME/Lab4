#Импорт библиотек 
import socket
import threading

host = '127.0.0.1'
port = 2022
users_limit = 3

def main():
    #socket = класс для обработки информации между процессами 
    #AF_INET = Использовании IPv4
    #SOCK_STREAM = Использование TCP-протокола, из-за его надежности
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #Подключиться серверу к данному порту, с таким названием хоста
        server.bind((host, port))
    except:
        print(f'Не удалось подключиться к порту {port} и хосту {host}')
        pass 
    server.listen(users_limit)

if __name__ == '__main__':
    main()
