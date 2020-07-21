from testing import tv
from pkg.helper.init import *
from pkg.helper.helper import *
# similarly other test modules
#from testing.tree import tree
#from testing.FileSearch import FileSearch
#from testing.XLS import xls
import logging





def test():

    init()
    log_debug("Testing Mode")

    if tv.__test__all__ or tv.__test__helper__:
        pass

    if tv.__test__all__ or tv.__test__tree__:
        tree.test()
    
    if tv.__test__all__ or tv.__test__FileSearch__:
        FileSearch.test()

    if tv.__test__all__ or tv.__test__xls__:
        xls.test()

