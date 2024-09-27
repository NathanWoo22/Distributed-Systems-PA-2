import numpy as np
import copy
import threading
from socket import *
import heapq
import time
import logging

def test_function():
    print("Hello World!")

class Maekawa():
    def __init__(self):
        return
    
    #thishost is an int and hosts is an array of pairs (ip, port)
    def GlobalInitialize(self, thishost, hosts):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='debug_log.log', encoding='utf-8', level=logging.DEBUG)
        self.numProcess = len(hosts)
        self.hosts = hosts
        self.myNum = thishost - 1
        self.processes = hosts
        self.vecClock = [0]*len(hosts)
        self.clockLock = threading.Lock()
        self.myAcks = [False]*len(hosts)
        self.acksLock = threading.Lock()
        self.myReleases = []
        self.releLock = threading.Lock()
        self.myRequests = []
        self.requLock = threading.Lock()
        self.criticalSection = threading.Lock()
        self.sentMessage = threading.Lock()
        self.voteGiven = False
        self.voteGivenLock = threading.Lock()
        self.sendSocket = socket(AF_INET,SOCK_DGRAM)
        #Last thing to happen
        self.listenSocket = socket(AF_INET, SOCK_DGRAM)
        self.listenSocket.bind(('', self.processes[self.myNum][1]))
        self.listenThread = threading.Thread(target= self.Listen, daemon=True)
        self.listenThread.start()
        return 

    def CreateSubsets(self):

        grid_size = int(np.ceil(np.sqrt(self.numProcess)))

        # Initialize grid to form subsets
        grid = np.arange(1, grid_size**2 + 1).reshape(grid_size, grid_size)

        # Remove any nodes outside the original
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] > self.numProcess:
                    grid[i][j] = -1
        
        subsets = {}
        count = 1
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
                
                print(f"Subset for process {count}: {subset}")

                if count == self.myNum + 1:
                    self.subset = subset 

                count += 1
        
        print(f"My subset (process {self.myNum}) is {self.subset}")
        return

    def QuitAndCleanup(self):
        return

    def MInitailize(self):
        return

    def MLockMutex(self):
        # Send request message to everyone but itself
        for host in self.subset:
            if host - 1 != self.myNum:
                thread = threading.Thread(target=self.MessageSending(host, 1), daemon=True)
                thread.start()
                thread.join()
                # self.MessageSending(host, 1) 

        # have a wait that checks if all have replied with an ack
        while True:
            allAckedFlag = True
            # Check  that each process has sent ack before returning
            for i, host in enumerate(self.subset):
                if host - 1 == self.myNum:
                    continue
                if self.myAcks[host-1] == False:
                    allAckedFlag = False
                    break
            if allAckedFlag:
                print("Recieved acks from all other subsets! Can now enter critical section")
                self.vecClock = [0]*len(self.hosts)
                return

            # time.sleep(1)
        # Once done waiting just return
        # return

    def MReleaseMutex(self):
        # Send release message to everyone but itself
        for host in self.subset:
            if host - 1 != self.myNum:
                self.MessageSending(host, 2) 

                
        return

    def MCleanup(self):
        return
    
    def receiveRequest(self, processID, curClock):
        # Queue up request
        # self.orderRequest(processID, curClock)
        # If only one request, ensure hasn't sent message anywhere else before sending message
        heapq.heappush(self.myRequests, (curClock, processID))
        
        self.voteGivenLock.acquire()
        # Sends the ack back to the process requesting, if vote not already given
        if self.voteGiven == False:
            self.voteGiven = True
            requestClock, processRequestAcked = heapq.heappop(self.myRequests)
            thread = threading.Thread(target=self.MessageSending(processRequestAcked - 1, 0))
            thread.start()
            thread.join()
        self.voteGivenLock.release()
        return
                
    def receiveRelease(self, processID, curClock):
        self.voteGivenLock.acquire()
        self.voteGiven = False
        if self.voteGiven == False:
            if len(self.myRequests) == 0:
                self.voteGiven = False
            else:
                self.voteGiven = True
                requestClock, processRequestAcked = heapq.heappop(self.myRequests)
                thread = threading.Thread(target=self.MessageSending(processRequestAcked, 0))
                thread.start()
                thread.join()
        self.voteGivenLock.release()
        return


    #updates order of requests based on clock info will block to obtain requLock
    def orderRequest(self, processID, curClock):
        self.requLock.acquire() 
        #check if requests is empty
        if not self.myRequests:
            self.myRequests.append((processID, curClock))
        else:
            inserted = False
            for i in range(len(self.myRequests)):
                curGreat = False
                compGreat = False
                compClock = self.myRequests[i]
                for j in range(len(curClock)):
                    if compClock[j] > curClock[j]:
                        compGreat = True
                    elif compClock[j] < curClock[j]:
                        curGreat = True
                #Current Clock is less than comparison clock
                if compGreat and not curGreat:
                    self.myRequests.insert(i, (processID, curClock))
                    inserted = True
                    break
            #Last in queue
            if not inserted:
                self.myRequests.append((processID))
        self.requLock.release()
        return
    
    #Should be started in a seperate thread
    def Listen(self):
        while 1:
            message, clientAddress = self.listenSocket.recvfrom(4096)
            composed = message.decode()
            decomposed = composed.split(sep= ',')
            if len(decomposed) == 3:
                #Update VecClock with new info
                processId = int(decomposed[0])
                clockVal = int(decomposed[1])
                messageVal = int(decomposed[2])
                self.clockLock.acquire()
                self.vecClock[processId] = max(self.vecClock[processId],clockVal)
                print(self.vecClock)
                curClock = copy.copy(self.vecClock)
                self.clockLock.release()
                if messageVal == 0:
                    self.logger.info(f"Received Ack from {processId}")
                    self.acksLock.acquire()
                    self.myAcks[processId] = True
                    self.acksLock.release()
                elif messageVal == 1:
                    self.logger.info(f"Received Request from {processId}")
                    self.receiveRequest(processId, curClock)
                elif messageVal == 2:
                    self.logger.info(f"Received Release from {processId}")
                    self.receiveRelease(processId, curClock)
                    # self.releLock.acquire()
                    # self.myReleases.append(processId)
                    # self.releLock.release()
        return

    #sendID should be integer corresponding to desired process to send too
    #Message should be an integer 0 for Ack 1 for Request 2 for Release
    #Handles self.vecClock intrementing
    def MessageSending(self, sendId, Message):
        #Header: Self Process ID (Location in inital Array) self clock end Header value
        #Message Either Ack or Request
        self.clockLock.acquire()
        self.vecClock[self.myNum] = self.vecClock[self.myNum] + 1
        sendAddress, sendPort = self.hosts[sendId - 1] # -1 to correct indexing error
        composed = f"{self.myNum},{self.vecClock[self.myNum]},{Message}".encode()
        self.logger.info(f"Sending message type {Message}: {(sendAddress,sendPort)}")
        self.sendSocket.sendto(composed, (sendAddress,sendPort))
        self.clockLock.release()
        return
