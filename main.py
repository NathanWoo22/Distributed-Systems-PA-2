# import DAP2_BrushWoo as dap
# from DAP2_BrushWoo import functional 
import DAP2.DAP2_BrushWoo.functional as fnl
# functional.test_function()
import numpy as np
import copy
import threading
from socket import *
import time

# listenThread = threading.Thread(target=Listen, daemon=True)
# listenThread.start()
maekawa =fnl.Maekawa()

maekawa.GlobalInitialize(2, [("ctb60-01", 5555), ("isengard", 5556)])

maekawa.CreateSubsets()
# while True:
    # time.sleep(1)
# time.sleep(2)
maekawa.MInitailize()
maekawa.MLockMutex()
print("Process 1 entering critical section")
maekawa.MReleaseMutex()
maekawa.MCleanup()
maekawa.QuitAndCleanup()