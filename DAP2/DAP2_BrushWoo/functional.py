import numpy as np

import threading
from socket import *

def main():
    print("Hello World!")

class Maekawa():
    def __init__(self):
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

    def CreateSubsets(selfself):

        grid_size = int(np.ceil(np.sqrt(self.numProcess)))

        # Initialize grid to form subsets
        grid = np.arange(1, grid_size**2 + 1).reshape(grid_size, grid_size)

        # Remove any nodes outside the original
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] > self.numProcess:
                    grid[i][j] = -1
        
        subsets = {}
        # Generate the subsets from the row column union
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == -1:
                    continue
                row = grid[i,:]
                col = grid[:,j]
                subset = set(row) | set(col)

                # Remove the -1's indicating no entries
                if (-1 in subset):
                    subset.remove(-1)
                
                subset = [int(x) for x in subset]
                print(subset)



        print(grid)
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
            composed = message.decode()
            decomposed = composed.split(sep= ',')
            if len(decomposed) == 3:
                print("message recieved")
                #Update VecClock with new info
                process = int(decomposed[0])
                clockVal = int(decomposed[1])
                messageVal = int(decomposed[2])
                self.clockLock.acquire()
                self.vecClock[process] = max(self.vecClock[process],clockVal)
                self.clockLock.release()
                match messageVal:
                    case 0:
                        print("Ack")
                        self.acksLock.acquire()
                        self.myAcks[process] = True
                        self.acksLock.release()
                    case 1:
                        print("Request")
                        self.requLock.acquire()
                        self.myRequests[process] = True
                        self.requLock.release()
                    case 2:
                        print("Release")
                        self.releLock.acquire()
                        self.myReleases[process] = True
                        self.releLock.release()
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