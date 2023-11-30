import hashlib, socket, sys, re, subprocess, hmac, os, pyfiglet, threading
from array import array
from datetime import datetime

openedFile = open(__file__,"r",encoding='utf-8')
readFile = openedFile.read()
progHash = hashlib.sha256(str(readFile).encode('utf-8')).hexdigest()
IO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IO.connect_ex(("255.255.255.255", 1337))

print(progHash)

chatLog = []

print("Please Input Your Display Name For This Session\n-----------------------------------------------")
displayName = re.sub('[^A-Za-z0-9]+', ' ', input())

while(True):
    newMsg = re.sub('[^A-Za-z0-9]+', ' ', input("~ "))
    chatLog.append(displayName + "@" + socket.getfqdn("localhost") + " : " + newMsg)

    os.system("cls")

    # Displaying the title banner
    ascii_banner = pyfiglet.figlet_format("Python Chat App")
    print(ascii_banner)

    for i in range(len(chatLog)):
        print(chatLog[i-1])
