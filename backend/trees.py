import numpy as np
import string
import random

def moveDown(array,parent,size,arrayID):
  child=2*parent+1
  temp=array[parent]
  temp2=arrayID[parent]

  while child<size:
    Max=array[child]
    Max2=arrayID[child]
    if child+1<size and array[child+1]>Max:
      child+=1
      Max=array[child]
      Max2=arrayID[child]
      
    if Max>temp:
      array[parent]=Max
      arrayID[parent]=Max2
      parent=child
    else:
      break
    child=2*parent+1

  array[parent]=temp
  arrayID[parent]=temp2
  

def heapSort(array,size,arrayID):
  for i in range(size//2-1,-1,-1):
    moveDown(array,i,size,arrayID)
  for i in range(size-1,0,-1):
    array[0],array[i]=array[i],array[0]
    arrayID[0],arrayID[i]=arrayID[i],arrayID[0]
    moveDown(array,0,i,arrayID)
  return arrayID

class treeNode(object):
  """docstring for treeNode"""
  def __init__(self, val):
    self.val=val
    self.right=None
    self.left=None
    self.ht=0
    
class avlTree(object):
  """dtype:
  string:'<U40'
  entero:'int64'
  flotante:'float64'
  """
  def __init__(self,dtype):
    self.root=None
    self.size=0
    self.array=None
    self.dtype=dtype
    
  def BF(self,root):      
    if root.right==None:
      rH=-1
    else:
      rH=root.right.ht
    if root.left==None:
      lH=-1
    else:
      lH=root.left.ht
    return lH-rH

  def actualH(self,root):
    if root.right==None:
      rH=-1
    else:
      rH=root.right.ht
    if root.left==None:
      lH=-1
    else:
      lH=root.left.ht
    root.ht=max(rH,lH)+1
    return root.ht

  def rLeft(self,root):
    right=root.right
    rightL=right.left

    right.left=root
    root.right=rightL

    self.actualH(root)
    self.actualH(right)
    return right

  def rRight(self,root):
    left=root.left
    leftR=left.right

    left.right=root
    root.left=leftR

    self.actualH(root)
    self.actualH(left)
    return left

  def insert(self,val):
    self.root=self.__insert(val,self.root)
    self.size+=1

  def __insert(self,val,root):
    
    if root==None:
      root=treeNode(val)
      return root

    if val<root.val:
      root.left=self.__insert(val,root.left)   
    
    elif val>root.val:
      root.right=self.__insert(val,root.right)

    
    self.actualH(root)
    bf=self.BF(root)
    
    if bf>1:
      if val>root.left.val:
        root.left=self.rLeft(root.left)
        return self.rRight(root)
    
      else:
        return self.rRight(root)
        

    if bf<-1:
      if val<root.right.val:
        root.right=self.rRight(root.right)
        return self.rLeft(root)

      else:
        return self.rLeft(root)
    
    return root

  

  def minVal(self,root):
    current=root
    while current.left != None:
      current=current.left
    return current

  def delete(self,val):
    try:
      self.root=self.__delete(val,self.root)
      self.size-=1
      return True
    except:
      return False
  def __delete(self,val,root):
    if root==None:
      return root

    if val<root.val:
      root.left=self.__delete(val,root.left)
    
    elif val>root.val:
      root.right=self.__delete(val,root.right)

    else:
      if root.left==None:
        temp=root.right
        root=None
        return temp
      elif root.right==None:
        temp=root.left
        root=None
        return temp
      temp=self.minVal(root.right)
      root.val=temp.val
      root.right=self.__delete(temp.val,root.right)

    self.actualH(root)
    bf=self.BF(root)

    if bf<-1:
      if self.BF(root.right)<=0:
        return self.rLeft(root)
      else:
        root.right = self.rRight(root.right)
        return self.rLeft(root)

    if bf>1:
      if self.BF(root.left)>=0:
        return self.rRight(root)
      else:
        root.left = self.rLeft(root.left)
        return self.rRight(root)

    return root        

  def search(self,root,val):
    current=root
    while current!=None and val!=current.val:
      if current.ht==0:
        return None
      if val<current.val:
        current=current.left
    
      elif val>current.val:
        current=current.right
    return current

  def __printTree(self,root):
    if root!=None:
      if root.left !=None:
        self.__printTree(root.left)
      self.array[self.cont]=root.val
      self.cont+=1
      if root.right !=None:
        self.__printTree(root.right)


  def printTree(self):
    self.array= np.zeros(self.size,dtype=self.dtype)
    self.cont=0
    self.__printTree(self.root)
    return self.array

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

"""a=avlTree('int64')
f=[]
for x in range(1000000):
  tem=random.randint(0,10000)
  a.insert(tem)
  if x%2==0:
    f.append(tem)

for y in f:
  a.delete(y)

print(a.printTree())"""


    