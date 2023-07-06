import socket
import threading


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # После подключения к серверу он должен отрправить сообщение 
            # если прислал'NICK' в ответ выслать свой Nickname
            message = client.recv(1024).decode('utf-8') #был 'ascii'
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)# после пересылки никнейма от сервера ожидаются сообщения других пользователей
        except:
            # Закрытие соединения в случае ошибки
            print("receive error occured!")
            # client.close()
            break

# отправка сообщения в чат
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        try:
            client.send(message.encode('utf-8'))
        except:
            print("write error occured!")    
            break

# Choosing Nickname
nickname = input("Type your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET - ipv4, SOCK_STREAM - tcp
client.connect(('127.0.0.1', 55555))# передаем кортеж, который представляет собой сокет



# Создаем 2 потока, которые в бесконечном цикле ждут сообщений / готовы к отправке сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()