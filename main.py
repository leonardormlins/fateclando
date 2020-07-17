from ghost.client import startClient as startGhostClient
from ghost.server import startServer as startGhostServer 
from leo.client import startClient as startLeoClient
from leo.server import startServer as startLeoServer

from threading import Thread
from time import sleep

if __name__ == "__main__":
    print("Who are you?")
    print("( 1 ) Leo\n( 2 ) Ghost")
    value = int(input())
    if value == 1:
        Thread(target=startGhostServer).start()
        print('Loading...')
        sleep(5)
        startLeoClient()
    elif value == 2:
        Thread(target=startLeoServer).start()
        print('Loading...')
        sleep(5)
        startGhostClient()
    else:
        print("Error: Wrong input!")