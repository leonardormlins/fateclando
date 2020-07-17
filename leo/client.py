import socket
import rsa

def encrypt_message(text, pub_key):
    return rsa.encrypt(
        text,
        rsa.PublicKey.load_pkcs1(pub_key, format='PEM')
    )

def capturePublicKey():
    filePath = '/home/leo/Documents/Fatec/5Semestre/Branquinho/fateclando/leo/leoPub.txt'
    file = open(filePath,'r')

    pub_key = ''
    for line in file:
        pub_key += line

    file.close()
    return pub_key

def startClient():
    SERVER = '127.0.0.1'
    PORT = 5021
    pub_key = capturePublicKey()
    tcp = socket.socket(socket.AF_INET,
    socket.SOCK_STREAM)
    dest = (SERVER, PORT)
    
    tcp.connect(dest)
    tcp.send(pub_key.encode('ascii'))
    
    print ('To get out just tap CTRL+C\n')
    msg = input()
    while msg != 'x':
        tcp.send(
            encrypt_message(msg.encode('ascii'), pub_key)
            )
        msg = input()

    tcp.close()