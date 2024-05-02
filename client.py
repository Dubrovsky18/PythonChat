import argparse
import socket
import sys
import threading
import time

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip_adress', default='194.31.173.242')
parser.add_argument('-p', '--port', default='30123')
args = parser.parse_args(sys.argv[1:])
ip = str(args.ip_adress)
porting = int(args.port)


def proces():
    load_str = "loading"
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = counttime = i = 0
    while counttime != 100:
        time.sleep(0.075)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
        res = ''
        for j in range(ls_len): res = res + load_str_list[j]
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()
        load_str = res
        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1


def recr():
    global nickname
    try:
        while True:
            data = client_socket.recv(1024)
            msg = data.decode('utf-8')
            if msg == 'process':
                thread = threading.Thread(target=proces)
                thread.start()
            elif msg == "This nickname already used":
                nickname = "---"
            else:
                print('\n Входящее сообщение:\n ', msg, '\n')
    except Exception:
        client_socket.close()
        quit()


def sent():
    client_socket.send(nickname.encode('utf-8'))
    try:
        while True:
            message = input(f'\n {nickname}---Ваше сообщение ------ \n')
            if message == 'q' or message == 'QUIT':
                print("Exiting chat...")
                break
            client_socket.send(message.encode('utf-8'))
    except Exception:
        print("Server closed")
    finally:
        client_socket.close()
        print("Connection closed")
        quit()


client_socket = socket.socket()
client_socket.connect((str(ip), int(porting)))
nickname = input("Your nickname: ")
thread = threading.Thread(target=recr)
thread.start()
thread_sent = threading.Thread(target=sent)
thread_sent.start()
