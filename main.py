# import DAP2_BrushWoo as dap
# from DAP2_BrushWoo import functional 
from functional import Maekawa
# functional.test_function()
import numpy as np
import copy
import threading
from socket import *
import time
import sys

processid = int(sys.argv[1])
maekawa =Maekawa()
maekawa.GlobalInitialize(processid, [("10.60.88.67", 5555), ("10.60.88.67", 5556)])
maekawa.CreateSubsets()
maekawa.MInitailize()
maekawa.MLockMutex()
print(f"Process {processid} entering critical section")
maekawa.MReleaseMutex()
maekawa.MCleanup()
maekawa.QuitAndCleanup()