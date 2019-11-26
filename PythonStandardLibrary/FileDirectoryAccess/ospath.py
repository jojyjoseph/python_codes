import os


testdirectory1='./testdirectory1'
testdirectory2='./testdirectory2'
testfile1='./testdirectory1/file1.txt'
testfile2='./testdirectory2/file2.txt'


print("Absolute path is " + os.path.abspath(testdirectory1))
print("Basename of testfile1 is " + os.path.basename(testfile1))
print("Comman path for testdirectory1 and testdirectory2 is " + os.path.commonpath((os.path.abspath(testdirectory1),os.path.abspath(testdirectory2))))
print("Comman prefix for testdirectory1 and testdirectory2 is " + os.path.commonprefix((os.path.abspath(testdirectory1),os.path.abspath(testdirectory2))))
print("Directory name of the testfile1 is " + os.path.dirname(os.path.abspath(testfile1)))
print("Path exists for testfile1 : " + str(os.path.exists(os.path.abspath(testfile1))))
print("Size of testfile1 is " + str(os.path.getsize(os.path.abspath(testfile1))))
print("Is absolute path for testfile1 : " + str(os.path.isabs(testfile1)))
print("Is testfile1  file ? : " +  str(os.path.isfile(testfile1)))
print("Is testfile1  directory ? : " +  str(os.path.isdir(testfile1)))
print("Join path testdirectory and testfile1 " + os.path.join(os.path.abspath(testdirectory1),os.path.basename(testfile1)))
print("Relative path to current directory " + os.path.relpath(os.path.abspath(testfile1), '..'))
print("Are testfile1 and testfile2 to same file : " + str(os.path.samefile(testfile1, testfile2)))
(head,tail)=os.path.split(os.path.abspath(testfile1))
print("split the file name path : " + head + ", " + tail)
(head,tail)=os.path.splitdrive(os.path.abspath(testfile1))
print("split the file name path into drive : " + head + ", " + tail)





