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
        self.dictNames = {}
        self.freeSpace = linkedQueue()

    def add(self, dataList):
        if self.size == self.capacity:
            self.capacity *= 2
            newdata = np.zeros((self.capacity,),dtype=object)
            newdata[:self.size] = self.data
            self.data = newdata


        if self.freeSpace.empty() == False:
          
          if dataList[0] in self.dictNames.keys():
            temp = self.data[self.search(dataList[0])]
            temp[3] = dataList[3] + temp[3]
          else:

            currentRef=self.freeSpace.dequeue()
            self.dictNames[dataList[0]] = currentRef
            self.data[currentRef] = dataList

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
        i = self.dictNames.get(name)
        return i
      else:
        print("No se encontró el item")

    def searcher(self,name):
      print(self.data[self.search(name)])

    def delet(self,name,amount = -1):
      if name in self.dictNames.keys():
        for i in range(self.size):
          y = self.data[i]
          if y != 0:
            if y[0] == name:
              if y[3] == 1 or amount == -1 or y[3] <= amount:
                self.data[i] = 0
                self.freeSpace.inqueue(i)
                self.dictNames.pop(name)
              else:
                y[3] -= amount
              break
      else:
        print("No se encontró el item")

    def bSort(self):
      ans= np.array(list(self.dictNames.keys()))
      n=len(ans)
      for i in range(n-1):
        for j in range(n-1-i):
          if ans[j]>ans[j+1]:
            temp=ans[j]
            ans[j]=ans[j+1]
            ans[j+1]=temp
      return ans
    def edit(self, index, list):
      self.dictNames[list[0]] = self.dictNames.pop(self.data[index][0])
      self.data[index] = list


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

class node:
  def __init__(self, data):
    self.data=data
    self.next=None

class linkedQueue:
  def __init__(self):
    self.head = None
    self.tail = None

  def inqueue(self,data):
    new_node = node(data)
    if self.head==None:
        self.head=new_node
    else:
        self.tail.next=new_node
    self.tail=new_node

  def empty(self):
    return self.head==None

  def dequeue(self):
    if self.empty():
      raise Exception("empty queue")
    else:
      ans=self.head.data
      self.head=self.head.next
      return ans

