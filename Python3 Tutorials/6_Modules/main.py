#importing modules
import module1
import package

#importing modules from package
from package import module2

#import modules from subpackages
from package.subpackage1 import module5

#The below gives error as no module4 exists
#from package.subpackage1 import module4

#This is the way to import modules and checking for exceptions
try:
    from package.module3 import *
    from package.module4 import *

except ImportError:
    print("main.py - package.module3 import error - Exception is thrown as module4 is not found")


def _main():
    print("Modules in python")
    module1.module1_function1()

    module2.package_module2_function1()
    package.module2.package_module2_function1()



    #calling module3 from package
    
    # can cal the below as it's defined in the __all__
    package_module3_function1()
    
    #can't call the below function as it's not defined in the __all__
    #package_module3_function2()

    module5.package_subpackage1_module5_function1()

def main():
    _main()


main()
