import hashlib, socket, sys, re, subprocess, hmac, os, pyfiglet, threading, array, datetime
from colorama import Fore, Back, Style, init

init()

openedFile = open(__file__,"r",encoding='utf-8')
readFile = openedFile.read()
progHash = hashlib.sha256(str(readFile).encode('utf-8')).hexdigest()
IO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IO.connect_ex(("255.255.255.255", 1337))

print(progHash)

chatLog = []

print("Please Input Your Display Name For This Session\n"+("-"*50))
displayName = re.sub('[^A-Za-z0-9]+', '-', input("~ "))

class Server:
    def start():
        return "Started Server"
    
class Client:
    def connect():
        return "Connected To Server"

while(True):
    newMsg = re.sub('[^A-Za-z0-9]+', ' ', input("~ "))
    chatLog.append(Fore.BLUE + displayName + "@" + socket.getfqdn("localhost") + " : "+ Fore.RESET + newMsg)

    os.system("cls")

    # Displaying the title banner
    ascii_banner = pyfiglet.figlet_format("P2Python")
    print(ascii_banner)

    for i in range(len(chatLog)):
        print(chatLog[i-1])
