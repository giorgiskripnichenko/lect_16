
import os
import json
def createFile(address,filename):
    os.makedirs(address)
    os.chdir(address)
    with open (filename, 'w') as file:
        print(file)
        file.close()


def readFile(filename):
    file = open(filename,'r')
    print(file)
    file.close()

def writeInFile(filename,dict1):
    file = open(filename,'w+')
    file.write(json.dumps(dict1))
    file.close()


address = 'c:/kopa/fgh'
filename = 'test.txt'
createFile(address,filename)

filename = 'c:/kopa/fgh/test.txt'
readFile(filename)


dict1 = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]
filename = 'c:/kopa/fgh/test.txt'
writeInFile(filename,dict1)