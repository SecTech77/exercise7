import os

def run(**arg):

    print("[*] Inside dirlister module")
    files = os.listdir(".")

    return str(files)
