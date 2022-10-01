#Импорт библиотек 
import socket
import threading

host = '127.0.0.1'
port = 2022
clients_limit = 3

def main():
    #socket = класс для обработки информации между процессами 
    #AF_INET = Использовании IPv4
    #SOCK_STREAM = Использование TCP-протокола, из-за его надежности
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #Подключиться серверу к данному порту, с таким названием хоста
        server.bind((host, port))
        print(f'Запуск сервера {host} {port}')
    except:
        print(f'Не удалось подключиться к порту {port} и хосту {host}')
        pass 
    #Лимит возможных подключений
    server.listen(clients_limit)
    #Постоянно принимать подключения
    while True:
        #Принимаем информацию о пользователе
        client_socket, client_connection_info = server.accept()
        client_host = client_connection_info[0]
        client_port = client_connection_info[1]
        print(f'Пользователь удачно подключился через порт {client_port} и хост {client_host} ')
if __name__ == '__main__':
    main()
