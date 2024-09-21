def main():
    print("Hello World!")


def GlobalInitialize():
    return 

def QuitAndCleanup():
    return

def MInitailize():
    return

def MLockMutex():
    return

def MReleaseMutex():
    return

def MCleanup():
    return

#sendID should be integer corresponding to desired process to send too
#Message should be an integer 0 for Ack 1 for Request 2 for Release
def MessageHandle(sendId, Message):
    #Header: Self Porcess ID (Location in inital Array) self clock end Header value
    #Message Either Ack or Request
    return

if __name__ == "__main__":
    main()