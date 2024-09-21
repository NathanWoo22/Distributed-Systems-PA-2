import threading
from socket import *

def main():
    print("Hello World!")

class Maekawa():
    def __init__():
        return
    
    #thishost is an int and hosts is an array of pairs (ip, port)
    def GlobalInitialize(self, thishost, hosts):
        self.numProcess = len(hosts)
        self.myNum = thishost
        self.processes = hosts
        self.vecClock = [0]*len(hosts)
        self.clockLock = threading.Lock()
        self.myAcks = [False]*len(hosts)
        self.acksLock = threading.Lock()
        self.myReleases = [False]*len(hosts)
        self.releLock = threading.Lock()
        self.myRequests = [False]*len(hosts)
        self.requLock = threading.Lock()
        self.sendSocket = socket(AF_INET,SOCK_DGRAM)
        #Last thing to happen
        self.listenThread = threading.Thread(target= self.Listen, daemon=True)
        self.listenThread.start()
        return 

    def CreateSubsets(self):
        # Determine size of the grid 
        return

    def QuitAndCleanup(self):
        return

    def MInitailize(self):
        return

    def MLockMutex(self):
        return

    def MReleaseMutex(self):
        return

    def MCleanup(self):
        return
    
    #Should be started in a seperate thread
    def Listen(self):
        listenSocket = socket(AF_INET, SOCK_DGRAM)
        listenSocket.bind(('',), self.hosts[self.myNum][1])
        while 1:
            message, clientAddress = listenSocket.recvfrom(4096)

        return

    #sendID should be integer corresponding to desired process to send too
    #Message should be an integer 0 for Ack 1 for Request 2 for Release
    #Handles self.vecClock intrementing
    def MessageSending(self, sendId, Message):
        #Header: Self Process ID (Location in inital Array) self clock end Header value
        #Message Either Ack or Request
        self.clockLock.acquire()
        self.vecClock[self.myNum] = self.vecClock[self.myNum] + 1
        sendAddress, sendPort = self.hosts[sendId]
        composed = f"{self.myNum},{self.vecClock[self.myNum],Message}".encode()
        self.sendSocket.sendto(composed, (sendAddress,sendPort))
        self.clockLock.release()
        return

if __name__ == "__main__":
    main()