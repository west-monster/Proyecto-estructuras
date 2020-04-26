# arreglos dinamicos con numpy vercion 3.0 alpha
# Nombre, precio, codigo de barras, cantidad , fecha

import numpy as np
import random
import string

class almacenamiento:
    def __init__(self):
        self.data = np.zeros((50,) ,dtype=object)
        self.capacity = 50
        self.size = 0
        self.references = 0
        self.freeSpace = []
        self.dictNames = {}

    def add(self, dataList):
        if self.size == self.capacity:
            self.capacity *= 2
            newdata = np.zeros((self.capacity,),dtype=object)
            newdata[:self.size] = self.data
            self.data = newdata
        if len(self.freeSpace) != 0:
          if dataList[0] in self.dictNames.keys():
            temp = self.data[self.search(dataList[0])]
            temp[3] = dataList[3] + temp[3]
          else:
            self.dictNames[dataList[0]] = self.freeSpace[0]
            self.data[self.freeSpace[0]] = dataList
            self.freeSpace.pop(0)

        else:
          if dataList[0] in self.dictNames.keys():
            temp = self.data[self.search(dataList[0])]
            temp[3] = dataList[3] + temp[3]
          else:
            self.dictNames[dataList[0]] = self.references
            self.data[self.size] = dataList
            self.size += 1
            self.references += 1

    def search(self,name):
      if name in self.dictNames.keys():
        for i in range(self.size):
          y = self.data[i]
          if y != 0:
            if y[0] == name:
              return i
      else:
        print("No se encontró el item")

    def searcher(self,name):
      print(self.data[self.search(name)])

    def delet(self,name):
      if name in self.dictNames.keys():
        for i in range(self.size):
          y = self.data[i]
          if y != 0:
              if y[0] == name:
                if y[3] == 1:
                  self.data[i] = 0
                  self.freeSpace.append(i)
                  self.dictNames.pop(name)
                else:
                  y[3] -= 1
              break
      else:
        print("No se encontró el item")


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

