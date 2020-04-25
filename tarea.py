# arreglos dinamicos con numpy vercion 2.0
# Nombre, precio, codigo de barras, cantidad

import numpy as np
import random
import string
from time import time


class almacenamiento:
    def __init__(self):
        self.data = np.zeros((50,) ,dtype=object)
        self.capacity = 50
        self.size = 0
        self.references = 1
        self.freeSpace = []
        self.dictNames = {"nombre": 0}

    def add(self, x):
        if self.size == self.capacity:
            self.capacity *= 2
            newdata = np.zeros((self.capacity,),dtype=object)
            newdata[:self.size] = self.data
            self.data = newdata
        if len(self.freeSpace) != 0:
          
          if x[0] in self.dictNames.keys():
            temp = self.data[self.search(x[0])]
            temp[3] = x[3] + temp[3]
          else:
            self.dictNames[x[0]] = self.references
            self.data[self.freeSpace[0]] = x
            self.references += 1
            self.freeSpace.pop(0)

        else:
          if x[0] in self.dictNames.keys():
            temp = self.data[self.search(x[0])]
            temp[3] = x[3] + temp[3]
          else:
            self.dictNames[x[0]] = self.references
            self.data[self.size] = x
            self.size += 1
            self.references += 1

    def search(self,x):
      if x in self.dictNames.keys():
        for i in range(self.size):
          y = self.data[i]
          if y[0] == x:
            return i
            break
      else:
        print("No se encontró el item")

    def searcher(self,x):
      print(self.data[self.search(x)])

    def delet(self,x):
      if x in self.dictNames.keys():
        for i in range(self.size):
          y = self.data[i]
          #posible error cuando self.data == 0
          if y[0] == x:
            self.data[i] = 0
            self.freeSpace.append(i)
            break
        self.dictNames.pop(x)
      else:
        print("No se encontró el item")

#fucnines add(lista), searcher(nombre del objeto), delet(nombre de objeto )

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
    


