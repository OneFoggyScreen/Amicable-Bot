#Logging Tools for Amicable Bot

#--------- Libaries ---------#

import sys, datetime     #Why
sys.path.append("../")      #Python?
from settings import *             #Why?

#--------- Code ---------#

def ABLog(Message):
    """Logs given message with time."""
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S - ") + str(Message))