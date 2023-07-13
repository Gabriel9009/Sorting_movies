import os
import re
import shutil
change = input("enter the folder you want to enter\n")
os.chdir("/home/gabriel/"+change)


list = list(os.listdir())
list1 = []
for i in list:
    if "2023" in i:
        list1.append(i)

os.mkdir("2023")
for j in list1:
            
        destination = "/home/gabriel/Vid/2023"
        shutil.move(j, destination)
        

