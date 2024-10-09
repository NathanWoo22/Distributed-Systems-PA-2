# import DAP2_BrushWoo as dap
# from DAP2_BrushWoo import functional 
from functional import Maekawa
# functional.test_function()
import numpy as np
import copy
import threading
from socket import *
import time

maekawa =Maekawa()
maekawa.GlobalInitialize(2, [("10.60.88.67", 5555), ("10.60.88.67", 5556)])
maekawa.CreateSubsets()
maekawa.MInitailize()
maekawa.MLockMutex()
print("Process 2 entering critical section")
maekawa.MReleaseMutex()
maekawa.MLockMutex()
print("Process 2 entering critical section")
maekawa.MReleaseMutex()
time.sleep(2)
maekawa.MCleanup()
maekawa.QuitAndCleanup()