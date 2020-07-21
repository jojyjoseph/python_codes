import logging
import os
import shutil


def log_info(msg):
    print("info : " + str(msg))
    logging.info(str(msg))

def log_warn(msg):
    print("warning : " + str(msg))
    logging.warning(str(msg))

def log_error(msg):
    print("error : " + str(msg))
    logging.error(str(msg))

def log_exception(msg):
    print("exception : " + str(msg))
    logging.error(str(msg))

def log_debug(msg):
    print("test : " + str(msg))
    logging.debug(str(msg))

def createDir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    return str(path)

def delFile(path):
    if os.path.exists(path):
        os.remove(path)



__all__ = ['log_info', 'log_warn', 'log_error', 'log_exception', 'log_debug', 'createDir', 'delFile']
