def moveDown(array,parent,size):
  child=2*parent+1
  temp=array[parent]
  
  while child<size:
    Max=array[child]

    if child+1<size and array[child+1]>Max:
      child+=1
      Max=array[child]

    if Max>temp:
      array[parent]=Max
      parent=child
    else:
      break
    child=2*parent+1

  array[parent]=temp



def heapSort(array,size):
  for i in range(size//2-1,-1,-1):
    moveDown(array,i,size)
  for i in range(size-1,0,-1):
    array[0],array[i]=array[i],array[0]
    moveDown(array,0,i)


class treeNode(object):
  """docstring for treeNode"""
  def __init__(self, val):
    self.val=val
    self.right=None
    self.left=None
    self.ht=0
    

def BF(root):      
  if root.right==None:
    rH=-1
  else:
    rH=root.right.ht
  if root.left==None:
    lH=-1
  else:
    lH=root.left.ht
  root.ht=max(rH,lH)+1
  return lH-rH

def rLeft(root,right):
  root.right=right.left
  right.left=root
  BF(root)
  BF(right)
  return right

def rRight(root,left):
  root.left=left.right
  left.right=root
  BF(root)
  BF(left)
  return left

def balance(root,val):
  bf=BF(root)
  
  if bf>1:
    if val>root.left.val:
      root.left=rLeft(root.left,root.left.right)
      return rRight(root,root.left)
  
    else:
      return rRight(root,root.left)
      

  if bf<-1:
    if val<root.right.val:
      root.right=rRight(root.right,root.right.left)
      return rLeft(root,root.right)

    else:
      return rLeft(root,root.right)
  
  return root

def insert(root,val):
  if root==None:
    root=treeNode(val)
    return root

  if val<root.val:
    root.left=insert(root.left,val)   
  
  elif val>root.val:
    root.right=insert(root.right,val)   
      
  return balance(root,val)

def minVal(root):
  current=root
  while current.left != None:
    current=current.left
  return current

def delete(root,val):
  if root==None:
    return root

  if val<root.val:
    root.left=delete(root.left,val)   
  
  elif val>root.val:
    root.right=delete(root.right,val)  

  else:
    if root.left==None:
      temp=root.right
      root=None
      return temp
    elif root.right==None:
      temp=root.left
      root=None
      return temp
    temp=minVal(root.right)
    root.val=temp.val
    root.right=delete(root.right,temp.val)

  return balance(root,val)

def search(root,val):
  current=root
  while val!=current.val:
    if current.ht==0:
      return False
    if val<current.val:
      current.left=current   
  
    elif val>current.val:
      current.right=current
  return True

def printTree(root):
  if root!=None:
    if root.left !=None:
      printTree(root.left)
    print(root.val)
    if root.right !=None:
      printTree(root.right)
    
