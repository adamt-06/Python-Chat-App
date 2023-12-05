import hashlib, socket, sys, re, subprocess, hmac, os, threading, array, datetime

if os.name == 'nt':
    os.system('py -m pip install "pyfiglet~=1.0.2" -q -q -q')
# for mac and linux(here, os.name is 'posix')
else:
    os.system('sudo python3 -m pip install "pyfiglet~=1.0.2" -q -q -q')

from colorama import Fore, Back, Style, init
import pyfiglet

class Server:
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port
        self.server_IO = None
        self.clients = []

    def start(self):
        self.server_IO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_IO.connect_ex(("255.255.255.255", 1337))
        self.server_IO.listen()

        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()

    def accept_connections(self):
        while True:
            client_IO, client_address = self.server_IO.accept()
            self.clients.append(client_IO)

            client_thread = threading.Thread(target=self.handle_client, args=(client_IO,))
            client_thread.start()

    def handle_client(self, client_IO):

        while True:
            try:
                # Receive data from the client
                data = client_IO.recv(1024).decode()

                if not data:
                    self.clients.remove(client_IO)
                    break

                self.broadcast(data, client_IO)

            except ConnectionResetError:
                self.clients.remove(client_IO)
                break
            
    def broadcast(self, message, sender_IO):
        for client_IO in self.clients:
            if client_IO != sender_IO:
                try:
                    # Send the message to the client
                    client_IO.send(message.encode())
                except ConnectionResetError:
                    # If there is a connection reset error, remove the client connection
                    self.clients.remove(client_IO)
    
class Client:
    def connect():
        return "Connected To Server"
    
init()

openedFile = open(__file__,"r",encoding='utf-8')
readFile = openedFile.read()
progHash = hashlib.sha256(str(readFile).encode('utf-8')).hexdigest()

print(progHash)

chatLog = []

print("Please Input Your Display Name For This Session\n"+("-"*50))
displayName = re.sub('[^A-Za-z0-9]+', '-', input("~ "))



while(True):

    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

    # Displaying the title banner
    print(Fore.GREEN + pyfiglet.figlet_format("P2Python") + "\n----------------------------------------------\nSay hi")

    for i in range(len(chatLog)):
        print(chatLog[i])

    newMsg = re.sub('[^A-Za-z0-9]+', ' ', input("~ "))
    chatLog.insert(len(chatLog), Fore.GREEN + displayName + "@" + socket.getfqdn("localhost") + " : "+ Fore.LIGHTBLACK_EX + newMsg)
