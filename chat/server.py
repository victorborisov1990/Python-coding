import socket
import threading

# Sending Messages To All Connected Clients
def broadcast(message):#функция пересылки новых сообщений всем участникам чата
    for client in clients:# каждому сокету в списке сокетов
        client.send(message)# будет выслано сообщение

# получение сообщений от клиентов
def handle(client): # для определенного сокета:
    while handling:# в бесконечном цикле
        try:
            # Broadcasting Messages
            message = client.recv(1024)# ожидаем сообщения с буффером 1024 байта
            broadcast(message)# при получении пересылаем всем остальным
        except ConnectionAbortedError:# если разорвано соединение с клиентом (бан и тд)
            print('разорвано соединение с клиентом')
            break    
        except:# в случае непредвиденной ошибки
            # нужно удалить из списка сокетов и никнеймов инфу о пользователе и закрыть соединение
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while receiving:
        # установка соединения
        client, address = server.accept()#когда устанавливается соединение нового клиента с сервером в client, address 
        # запишутся из кортежа сокет (объект) и сокет в текстовом представлении (адрес + порт)
        print("Connected with {}".format(str(address)))# сообщение в консоль сервера о подключении с адреса ...

        # сохранение никнейма и сокета
        client.send('NICK'.encode('utf-8'))#после установления нового соединения в сокет (клиенту) отправляется
        # сообщение 'NICK' в кодировке асски
        nickname = client.recv(1024).decode('utf-8')#ожидается, что клиент пришлет в ответ свой никнейм
        if nickname not in nicknames:#если никнейм не занят
            nicknames.append(nickname)# добавление никнейма нового участника
            clients.append(client)# добавление сокета нового участника
            # списки никнеймов и сокетов добавляются новые элементы, они будут иметь одинаковый индекс

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))# сообщение в консоль сервера о новом никнейме
            broadcast("{} joined!".format(nickname).encode('utf-8'))#сообщение в общий чат о новом участнике
            client.send('Connected to server!'.encode('utf-8')) # сообщение новому участнику, что он подключился

            # Создание отдельного потока для нового клиента
            thread = threading.Thread(target=handle, args=(client,))# поток с функцией получения сообщений от указанного клиента
            thread.start()# запуск потока
        else:#если никнейм занят
            print("{} trying to join chat with used nickname. Disconnected".format(str(address)))
            client.send('Nick is buisy. Try later'.encode('utf-8'))
            client.close()


def admin():
    global admining
    global receiving
    global handling
    def show_clients():
        print('client of chat:')
        for nickname in nicknames:
                print('{}. {}'.format(nicknames.index(nickname),nickname))
    while admining:
        command = input('Enter command: 1 - show clients, 2 - ban, 3 - exit\n')
        if command == '1':
            show_clients()
        elif command == '2':
            show_clients()
            print('choose No of user to ban')
            index = int(input())
            # добавить трай кэтч на ввод не числа  и проверку на присутствие индекса в массиве
            client = clients[index]#выбираем сокет для дальнейшего закрытия
            clients.pop(index)# удаляем из списка сокетов
            client.close()#закрываем сокет
            nickname = nicknames[index]
            broadcast('{} has banned!'.format(nickname).encode('utf-8'))
            nicknames.pop(index)
        else:
            for client in clients:
                client.send('chat is closing. goodbye'.encode('utf-8'))
                client.close
            handling = False    
            receiving = False
            admining = False
            print('server is shutting down')
        # Нужно здесь закрыть все соединения? или просто завершить основной процесс?

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET - ipv4, SOCK_STREAM - tcp
server.bind((host, port)) # настройка адреса и порта на сокете
server.listen()# начать прослушивание (ожидать вход подключение)

# Lists For Clients and Their Nicknames
clients = [] # список сокетов (адреса и порты серверов и клиентов)
nicknames = [] # список никнеймов соответствующих сокетам

receiving = True
admining = True
handling = True

print("Server is listening...")
# receive()
receive_thread = threading.Thread(target=receive)
receive_thread.start()

admin_thread = threading.Thread(target=admin)
admin_thread.start()

receive_thread.join()
admin_thread.join()
print('Goodbye')