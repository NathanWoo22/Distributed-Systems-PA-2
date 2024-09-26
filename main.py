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

maekawa.GlobalInitialize(1, [("ctb60-01", 5555), ("isengard", 5556)])

maekawa.CreateSubsets()
# while True:
    # time.sleep(1)
# maekawa.MLockMutex()
# maekawa.MReleaseMutex()