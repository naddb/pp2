'''
Write a Python program to check for
 access to a specified path. Test the existence
 , readability, writability and executability of the specified path
'''
import os
def path_check(path):
    print(path,end='\n')
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))
path_check('C:/Users/Админ/OneDrive/Рабочий стол/python lectures/lecture 6')
path_check('C:/Users/Админ/OneDrive/Рабочий стол/python lectures/NOSuchLECTURE')
path_check('C:/Users/Админ/OneDrive/Рабочий стол/книги по англу')
