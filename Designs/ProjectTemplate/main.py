from config import gv
from pkg.helper.init import *
import logging
from testing.test import test


def __main():
    init()
    logging.debug("Starting .....")



def main():

    if not gv.__testing__:
        __main()
    else:
        test()


#main function starts here
main()
        




