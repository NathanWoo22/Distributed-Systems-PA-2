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
maekawa.GlobalInitialize(1, [("8.8.8.8", "5555"), ("8.8.8.8", "5555"), ("8.8.8.8", "5555")])
maekawa.CreateSubsets()