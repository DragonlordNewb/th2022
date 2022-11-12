import os

def installPackage(name):
    os.system("py -m pip install " + name)
