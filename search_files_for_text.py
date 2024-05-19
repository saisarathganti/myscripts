# Find file which has the given text in a given directory

import os

text = input("Enter the text to find:\n")
path = input("Enter the folder path to search in:\n")

def getFiles(path):
    flag = False
    os.chdir(path)
    files = os.listdir()
    for file_name in files:
        if file_name == ".git":
            continue
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getFiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(abs_path, "r")
            # print(f.read())
            if text in f.read():
                flag = True
                print(text + " found in " + abs_path + ".")
                return True
    if flag == False:
        print(text + " not found in " + path + ".")
        return False

getFiles(path)
