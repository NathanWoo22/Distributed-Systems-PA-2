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
# maekawa.GlobalInitialize(processid, [("localhost", 5555), ("localhost", 5556), ("localhost", 5557), ("localhost", 5558), ("localhost", 5559)])
# maekawa.GlobalInitialize(processid, [("localhost", 5555), ("localhost", 5556), ("localhost", 5557)])
maekawa.GlobalInitialize(processid, [("localhost", 5555), ("localhost", 5556)]) 
maekawa.MInitailize()
# time.sleep(5)
maekawa.MLockMutex()
print(f"Process {processid} entering critical section")
maekawa.MReleaseMutex()
maekawa.MCleanup()
maekawa.QuitAndCleanup()