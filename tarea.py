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
        self.tam = 0
        self.nom = 1
        self.dispo = []
        self.jisho = {"nombre": 0}

    def add(self, x):
        if self.tam == self.capacity:
            self.capacity *= 2
            newdata = np.zeros((self.capacity,),dtype=object)
            newdata[:self.tam] = self.data
            self.data = newdata
        if len(self.dispo) != 0:
          
          if x[0] in self.jisho.keys():
            temp = self.data[self.search(x[0])]
            temp[3] = x[3] + temp[3]
          else:
            self.jisho[x[0]] = self.nom
            self.data[self.dispo[0]] = x
            self.nom += 1
            self.dispo.pop(0)

        else:
          if x[0] in self.jisho.keys():
            temp = self.data[self.search(x[0])]
            temp[3] = x[3] + temp[3]
          else:
            self.jisho[x[0]] = self.nom
            self.data[self.tam] = x
            self.tam += 1
            self.nom += 1

    def search(self,x):
      if x in self.jisho.keys():
        for i in range(self.tam):
          y = self.data[i]
          if y[0] == x:
            return i
            break
      else:
        print("No se encontró el item")

    def searcher(self,x):
      print(self.data[self.search(x)])

    def delet(self,x):
      if x in self.jisho.keys():
        for i in range(self.tam):
          y = self.data[i]
          #posible error cuando self.data == 0
          if y[0] == x:
            self.data[i] = 0
            self.dispo.append(i)
            break
        self.jisho.pop(x)
      else:
        print("No se encontró el item")

#fucnines add(lista), searcher(nombre del objeto), delet(nombre de objeto )

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
    


