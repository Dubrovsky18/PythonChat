import argparse
import socket
import sys
import threading
import time

list_dict_client = {}
list_listen = []
list_nickname = []
list_dict_nickname = {}
broadcast_from_bot = "General information"


def delete(client):  # Function to delete users, who went out
    nickname_client = list_dict_nickname[client]
    del list_dict_nickname[client]
    list_nickname.remove(nickname_client)
    try:
        list_listen.remove(client)
    except Exception:
        print(f"{nickname_client} go out - he don't listen broadcast")
    del list_dict_client[nickname_client]


def send(to_client, msg):  # Separate function to send the message
    to_client.send(msg.encode('utf-8'))


def recv(client):  # Separate message receiving function
    msg = client.recv(1024).decode('utf-8')  # Get message from client
    if msg == 'q' or msg == 'QUIT':  # Checking in quiting user
        send(client, 'Disconnected')
        print(f'Disconnected : {list_dict_nickname[client]}')  # Our log
        delete(client)  # Delete in every dict and list
        client.close()
        return False
    elif msg in ['TELL', 'LIST', 'QUIT', 'HELP']:  # Checking in special word
        word(client, msg)
    else:
        return msg


def send_to_broadcast(nickname, msg):  # Separate function for broadcast communication
    if msg != 'None':
        for client in list_listen:  # Realization broadcast message
            send(client, f"(broadcast) {nickname}: {msg}")


def start_server():
    while True:
        client_socket, address = server_socket.accept()  # we accept all connections to server
        print('Connected by' + str(address))  # our local logs
        thread = threading.Thread(target=welcome, args=(
        client_socket,))  # Process boring user to chat with other users, then we can retrun to listen new connected users
        thread.daemon = True  # Our users will be in chat until they wnat to go out
        thread.start()  # start Proceess


def authoruzation(client):  # Function for authoruzation user
    while True:  # Ask until there is a result
        nickname = recv(client)  # Ask client about nickname
        if not nickname in list_dict_client:  # Check nickname in list of nicknames
            send(client, "Successfully")
            break
        elif nickname == 'q':  # If client want to exit
            send(client, "Disconnected")
            client.close()  # If client quit from chat, server close this client
            break
        else:
            send(client, "This nickname already used ")  # Option if there is already such nickname
    return nickname


def welcome(client):
    nickname = authoruzation(client)  # Nick from client, witch connected

    list_dict_client[nickname] = client  # Add Nick and client to dict with key - nickname
    list_dict_nickname[client] = nickname  # Add socket and nickname in dict with key - client
    list_nickname.append(nickname)  # Add nicknames for present list of nicknames

    with open('chat_log', 'a') as f:
        f.write(f"(Log) {client} : {nickname}")  # Just information for admin in server
    send_to_broadcast(broadcast_from_bot,
                      f"{nickname} has joined the Chat")  # Broadcast message about user, witch added to chat
    send(client, 'process')  # function in client, for some waiting(animation)
    time.sleep(1)
    send(client, """Welcome to the chat room. 
This chat is unique, here you can communicate both privately and in general chat. 
you are given a choice of 1 - for private messages.
If you want to communicate with your friend, we advise you to wait a few seconds, and then press 1.
2 - General Chat. Here you will communicate with all the guys in the group. A list of available commands:
    TELL       Send a private message to somebody (/tell:user:message)
    LIST       Display users in chat
    QUIT       go out from chat
    """)
    time.sleep(2)
    send(client,
         "What are you want: 1. send to one user or 2. inside to group ")  # Each client can choose(private message)
    num = recv(client)
    if num == "1":  # choice mode with private message
        client_to_one_connect = choose_for_one(client)  # User need choose interlocutor
        chat(client, client_to_one_connect)  # function for privet chat (from whom, to whom, flag for private message)
    else:
        list_listen.append(client)  # User added to list, witch tell, who will get message
        send(client, " You in group ")
        chat(client)


def choose_for_one(client):
    string_choose = ""
    list_choose = []
    i = 0
    for i, key in zip(range(len(list_dict_client.keys())), list_dict_client.keys()):  #
        string_choose += '{0}.{1}'.format(i + 1, key) + " "
        list_choose.append(string_choose)
    while True:
        send(client, f"Choose your user-chat \n {string_choose} ")
        usernum = recv(client)
        usernum = int(usernum)
        if 0 < usernum <= len(list_dict_client.keys()):
            choose_user = ''
            for i in range(len(list_choose)):
                try:
                    choose_user = list_nickname[usernum - 1]
                except Exception:
                    print(f"{list_dict_nickname[client]} stupid and can't choose number ")
            if choose_user:
                send(client, "Successful")
                return list_dict_client[choose_user]
            else:
                send(client, '\n Nobody in chat')


def word(client, message):
    nick = list_dict_nickname[client]
    if message == 'TELL':  # Receive a private message
        send(client, f"Who will get your message? \n {list_nickname} \n")
        username = recv(client)
        chat(client, list_dict_client[username], True)
    elif message == 'LIST':  # Message with a list of nicknames
        send(client, f'Users in chatroom: {list_nickname}')
    elif message == 'HELP':  # Message with a list of available commands
        send(client, '''
    A list of available commands:
    TELL       Send a private message to somebody (/tell:user:message)
    LIST       Display users in chat
    QUIT       go out from chat
                    ''')
    else:
        return True


def chat(client_from, client_to=None, flag=False):
    while True:
        try:
            message = recv(client_from)
            if not message:
                flag = True
            nick = list_dict_nickname[client_from]
            if client_to is not None:
                send(client_to, f"(private) {nick} : {message}")
                if flag:
                    break
            else:
                send_to_broadcast(nick, message)
        except Exception:
            print('break from ', client_from)


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip_address', default='127.0.0.1')
parser.add_argument('-p', '--port', default='12345')
args = parser.parse_args(sys.argv[1:])
ip = str(args.ip_address)
porting = int(args.port)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, porting))
    server_socket.listen()
    print('Server started to work')
    try:
        start_server()
    except KeyboardInterrupt:
        print('How rude of you \n')
        server_socket.close()
        quit()
