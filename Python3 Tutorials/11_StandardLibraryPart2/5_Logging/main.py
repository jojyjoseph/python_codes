from LoggerPackage import init
from LoggerPackage.helper import *

def _main():
    print("Python - logger reference example")
    init.init()
    
    #Info based log
    log_info("Log Info message")

    #Warning based log
    log_warn("Log Warn message")

    #log_error
    log_error("Log error message")

    #log_exception
    log_exception("Log exception message")

    #log_debug
    log_debug("Log debug messasge")

def main():
    _main()

main()
