import os 
import random
import string

def Randomize(path):
    directory = os.scandir(path)
    for item in directory:
        if os.path.isdir(item):
            Randomize(item)
    directory = os.scandir(path)
    for item in directory:
        if os.path.isfile(item):
            if item.name == 'Randomizer.py':
                break
            if isinstance(path,str):
                temp = path
            else:
                temp = path.path
            os.rename(item,temp+'\\'+''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5,30)))+'.'+item.name.split('.')[1])
Randomize(".")