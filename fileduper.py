import os
import sys

i = 1

path1 = input("Where is the file: ")
path2 = input("Where do you want it: ")
copies = int(input("How many files: "))

while i <= copies:
    i += 1
    temp = "cp " + path1 + " " + path2 + str(i)
    os.system(temp)
    #print(str('mv'+path1+' '+path2+i))
