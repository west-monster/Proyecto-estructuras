
from datasql import *
import trees
import json
import numpy as np

class almacen():
	"""docstring for almacen"""
	def __init__(self):
		#info=all_col('nombre')
		self.tree=trees.avlTree('<U40')
		#for x in info:
		#	self.tree.insert(x)
		self.fromJson()

	def fromJson(self):
		with open('tree.json', 'r') as file:
			string=file.read()
		jsonData=json.loads(string)
		self.tree.root=self.__fromJson(jsonData)

	def __fromJson(self,json):
		root=trees.treeNode(json["val"])
		if json["left"] != None:
			root.left=self.__fromJson(json["left"])
		if json["right"] != None:
			root.right=self.__fromJson(json["right"])
		self.tree.actualH(root)
		return root
		

	def toJson(self):
		self.json=self.__toJson(self.tree.root)
		with open('tree.json', 'w') as file:
			json.dump(self.json,file,indent=4)

	def __toJson(self,root):
		if root!=None:
			left,right=None,None
			if root.left !=None:
				left=self.__toJson(root.left)
			if root.right !=None:
				right=self.__toJson(root.right)
			json={"val":root.val,"left":left,"right":right}
			return json

	def deleteInf(self,name):
		if self.tree.delete(name):
			delet(name)
			return True
		return False

	def search(self,name):
		return self.tree.search(name)

	def sortBy(self,column):
		if column=="nombre":
			Sorted= self.tree.printTree()
		elif column=="fecha":
			return None
		else:
			toSort=all_col(column)
			names=all_col('nombre')
			Sorted=trees.heapSort(toSort,self.tree.size,names)
		temp=[]
		with open('jorg_'+column[0].lower()+'.json', 'w') as file:
			for i in Sorted:
				producto=getRaw(i)[0]

				obj={"ID":producto[0],"nombre":producto[1],"precio":producto[2],"codigo":producto[3],"cantidad": producto[4],"fecha": producto[5]}
				temp.append(obj)
			json.dump(Sorted,file,indent=4)



class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class linkedlist:
	def __init__(self):
		self.head = None
		self.cantidad = 0

	def add(self, newval):
		newnode = node(newval)
		if not self.head:
			self.head = newnode
			self.cantidad += 1
			return
		initnode = self.head
		while initnode.next is not None:
			initnode = initnode.next
		initnode.next = newnode
		self.cantidad += 1


	def mostrar(self):
		printval = self.head
		while printval is not None:
			print(printval.data)
			printval = printval.next


class stack:
	def __init__(self):
		self.lista2 = linkedlist()

	def add2(self,value):
		if self.lista2.cantidad < 5:
			self.lista2.add(value)
		else:
			self.lista2.head = self.lista2.head.next
			self.lista2.add(value)

	def unstack(self):
		if self.lista2.head and self.lista2.cantidad != 0:
			if self.lista2.head.data is not None:
				a = self.lista2.head.data
			if self.lista2.head.next is not None:
				self.lista2.head = self.lista2.head.next
				self.lista2.cantidad -= 1
			else:
				self.lista2.head = None
				self.lista2.cantidad -= 1
			return a
		else:
			return



class queue():

	def __init__(self):
		self.pila1 = stack()
		self.pila2 = stack()

	def add3(self,newval):
		self.pila1.add2(newval)
		self.pila2.add2(self.pila1.unstack())

	def desizing(self):
		a = self.pila2.unstack()
		return a

n = queue






#for x in range(10000):
#	insert(randomword(4),3.36,4,5)

#a.sortBy("Nombre")

	