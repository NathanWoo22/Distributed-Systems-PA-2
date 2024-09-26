# import DAP2_BrushWoo as dap
# from DAP2_BrushWoo import functional 
import DAP2.DAP2_BrushWoo.functional as fnl
# functional.test_function()
import numpy as np
import copy
import threading
from socket import *

# listenThread = threading.Thread(target=Listen, daemon=True)
# listenThread.start()

maekawa =fnl.Maekawa()
maekawa.GlobalInitialize(1, [("isengard", 5555), ("localhost", 5556), ("localhost", 5557)])
maekawa.CreateSubsets()
maekawa.MLockMutex()
maekawa.MReleaseMutex()