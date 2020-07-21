import logging
import shutil
import os
from pkg.helper.helper import *

def dellogfile():
    if os.path.exists('./logfile'):
        os.remove('./logfile')

def logfileinit():
    dellogfile()
    logging.basicConfig(filename='logfile', level=logging.DEBUG)

def init():
    logfileinit()
    createDir('./tmp')


__all__=['init']

