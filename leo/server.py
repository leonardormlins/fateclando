#server.py - Leo
import socket
import rsa
from threading import Thread

global public_key
global private_key

def capturePrivateKey():
    filePath = '/home/leo/Documents/Fatec/5Semestre/Branquinho/fateclando/leo/leoPri.txt'
    file = open(filePath,'rb')
    private_key = bytes()
    for line in file:
        private_key += line
    file.close()
    return private_key

def decryptMessage(msgc):
    private_key = capturePrivateKey()
    return rsa.decrypt(
        msgc,rsa.PrivateKey.load_pkcs1(private_key, format='PEM')
        )

def connection(con,cli):
    while True:
        msg = con.recv(1024)
        if b'-----BEGIN RSA PUBLIC KEY-----' in msg:
            public_key = msg
        else:
            toPrint = str(decryptMessage(msg))
            toPrint[0] = '' 
            print('Ghost: ', toPrint)
        if not msg: 
            break

    print ('Closing client connection...', cli)
    con.close()

def startServer():
    HOST = '127.0.0.1'
    PORT = 5021

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)

    tcp.bind(orig)
    tcp.listen(1)
    
    while True:
        con, client = tcp.accept()
        print ('Connected by ', client)
        t = Thread(target=connection, args=(con,client,))
        t.start()