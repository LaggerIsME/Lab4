#Импорт библиотек 
import socket
import threading

host = '127.0.0.1'
port = 2022
clients_limit = 3
actual_clients = [] #Список пользователей

#Ожидание сообщения
def listen_for_msg(client_socket, sender_username):
    
    while True:
        msg = client_socket.recv(2048).decode('utf-8')
        if msg == '':
            print(f'Сообщение от {sender_username} пустое')
        else:
            chat_msg = sender_username + ": " + msg 
            send_message_to_all(chat_msg)
#Отправка сообщений одному пользователю
def send_message_to_client(client_socket, msg):
    
    client_socket.sendall(msg.encode())

#Отправка сообщений всем пользователям
def send_message_to_all(msg):
    
    for user in actual_clients:
        send_message_to_client(user[1], msg)

#Обращение к клиенту
def client_handler(client_socket):
    
    #Сервер ждет прозвища пользователя с максимальной длиной 100
    while True:
        username = client_socket.recv(2048).decode('utf-8')
        if username == '':  
            print('Никнейм пуст')
        else:
            actual_clients.append((username, client_socket))
            connect_msg = "SERVER: " + f"{username} зашел(-ла) в чат"
            send_message_to_all(connect_msg)
            break

    threading.Thread(target=listen_for_msg, args = (client_socket, username, )).start()

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
        
        threading.Thread(target = client_handler, args = (client_socket, )).start()

if __name__ == '__main__':
    main()
