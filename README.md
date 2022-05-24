# Курс "Основы программирования"

# Список заданий
- [X] Описание теории
- [X] Создать список пользователей(*Создать Базу данных)
- [X] Создать общение пользователей друг с другом, а не с сервером. 
- [X] При подключении отображать пользователей на выбор
- [X] Создать описания кода и оформить код

# Структура 
- [X] Описание работы
- [X] Теоритическая часть
- [X] Практическая часть
- [X] Фотографии работ
- [X] Выводы




Задача, которая нам поступила
-----------------------------
Создать чат через программный интерфейс для обеспечения информационного обмена между процессами - socket. Сервер должен принимать сообщение от опредленного пользователя и отправлять другому. 

Установка чата к себе на компьютер

1. Клонируем репозиторий
```sh
git clone https://github.com/Dubrovsky18/PythonChat.git
```

2. Выполняем команду
```sh
sh PythonChat/download.sh
```
* Совет: закрыть консоль и снова открыть 

3. Запускаем сервер
```sh
chat-server
```

4. Запускаем клиента (один/множество раз)
```sh
chat
```

* Если не сработает тогда заходим в папку, которую копировали из github и запускаем

3. Запуск сервера
```sh
python3 server.py
```

4. Запуск клиента
```sh
python3 client.py
```

Теоретическая часть
--------------------------
Существует 2 вида socket:
* Серверный - принимающая сторона
* Клиентский - отправляющая сторона

В данном случае у нас клиенты будут отправлять всё серверу и получать от сервера.
Socket рабоает на транспортном уровне:
* Потоковый (TCP) - сокеты установив двусторонней соединение, передат поток байтов.
* Дейтаграммные(UDP) - сокету не требуют явного подключения между ними

Socket состоит из Ip-адреса и Port.

Для написания проекта выделим то, что нам нужно:
* Строгая последовательность команд для сервера и клиента
* Параллельное выполнения процессов - Асинхроность(выполнение задач независимо от других процессов)
* Обработка ошибок

В решении данного задания стоит знать базовые понятия потока и процесса

* Поток рабоает внутри процесса
* Потоки позволяют запустить выполнение нескольких задач в конкурентном режиме в рамках одного процесса интерпретатора.

* Процесс - запущенная программа. Процессу выделяются отдельные ресурсы: память, процессорное время поток (thread) - это единица исполнения в процессе.
* Потоки разделяют ресурсы процесса, к которому они относятся.


Практическая часть
----------------------------
Сервер
======

```sh
# Импортируем нужные модули
import argparse
import socket
import sys
import threading
import time

# Списки и Словари для удобного поиска пользователей 
list_dict_client = {}
list_listen = []
list_nickname = []
list_dict_nickname = {}

# Функция для удаление пользователя, если он выйдет из чата
def delete(client): 

# Функция для отправки сообщения
def send(to_client, msg):

# Функция для принятия сообщения и обработки специальных команд
def recv(client): 

# Функция для общего чата
def send_to_broadcast(nickname, msg):

# Функция для ожидания подключения пользователя и отправки его в отдлеьный поток
def start_server()

# Функция для авторизации пользователя, чтобы не было одинаковых NICKNAME
def authoruzation(client)

# Функция для приветствия нового пользователя и предоставить ему выбор режима чата
def welcome(client):

# Функция которая дает пользователю выбрать себе собеседника
def choose_for_one(client):

# Функция специальных слов
def word(client, message):

# Функция самого чата, в котором происходят все беседы
def chat(client_from, client_to=None, flag=False):

# При запуске команды chat-server можно указать флаги ip-адреса и/или порта, по которому подключатся
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip_address', default='127.0.0.1')
parser.add_argument('-p', '--port', default='12345')
args = parser.parse_args(sys.argv[1:])
ip = str(args.ip_address)
porting = int(args.port)

# Оснвоной вызов программы
if __name__ == '__main__':
```

Клиент
======
```sh
# # При запуске команды chat можно указать флаги ip-адреса и/или порта, по которому подключатся
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip_adress', default='127.0.0.1')
parser.add_argument('-p', '--port', default='12345')
args = parser.parse_args(sys.argv[1:])
ip = str(args.ip_adress)
porting = int(args.port)

# Функция анимации ожидания
def proces()

# Функция принятия сообщаний
def recv():

# Функция отправки сообщений
def sent():

# Основной модуль подключения
client_socket = socket.socket()
client_socket.connect((str(ip), int(porting)))
nickname = input("Your nickname: ")
thread = threading.Thread(target=recv)
thread.start()
thread_sent = threading.Thread(target=sent)
thread_sent.start()
```



Фотографии работ
=================
![Alt text](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/task.jpg "Task")











\
--------------------------

![Alt text](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/web1.png "сайт на web1")
![Alt-текст](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/web2.png "Сайт на web2")
--------------------------

+ Забиваем адрес - Virtual IP([Немного о Keepalived и VI](https://www.servers.ru/knowledge/linux-administration/how-to-setup-floating-ip-using-keepalived)). Если при каждом обновлении он показывает сайт web1, а потом web2, поочередно, следовательно мы сделали все правильно.

\
-------------------------

![Alt-текст](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/haproxy_web1.png "Web1 in haproxy")
![Alt-текст](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/haproxy_web2.png "Web2 in haproxy")
---------------------------


### Проверка на отказоустойчивость
==================================

+ Выключаем один из backend-server(желательно, чей приоритет выше). Забиваем адрес - Virtual IP. Если при каждом обновлении он показывает сайт web1, а потом web2, поочередно, следовательно мы сделали все правильно.

\
---------------------
![Alt-текст](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/failover/haproxy1_web1.png "Отказоустойчивасть. Web1 - Основа на haproxy1")
![Alt-текст](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/failover/haproxy1_web2.png "Отказоустойчивасть. Web2 - Основа на haproxy1")
---------------------------



+ Включаем один сервер, выключаем другой. Забиваем - Virtual IP.Если при каждом обновлении он показывает сайт web1, а потом web2, поочередно, следовательно мы сделали все правильно.

\
---------------------
![Alt-текст](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/failover/haproxy2_web1.png "Отказоустойчивасть. Web1 - Основа на haproxy2")
![Alt-текст](https://github.com/Dubrovsky18/OS_system/blob/main/project_5/report/failover/haproxy2_web2.png "Отказоустойчивасть. Web2 - Основа на haproxy2")
---------------------------
