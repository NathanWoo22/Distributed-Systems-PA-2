# import DAP2_BrushWoo as dap
# from DAP2_BrushWoo import functional 
import DAP2.DAP2_BrushWoo.functional as fnl
# functional.test_function()
import numpy as np
import copy
import threading
from socket import *
import time

maekawa =fnl.Maekawa()
maekawa.GlobalInitialize(1, [("10.60.68.172", 5555), ("isengard", 5556)])
maekawa.CreateSubsets()
maekawa.MInitailize()
maekawa.MLockMutex()
print("Process 1 entering critical section")
maekawa.MReleaseMutex()
maekawa.MCleanup()
maekawa.QuitAndCleanup()