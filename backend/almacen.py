from structures import randomword
from datasql import *
import trees
import json
import numpy as np
from os import remove
from os import path
import main
class almacen():
	"""docstring for almacen"""
	def __init__(self):

		self.tree=trees.avlTree('<U40')
		if not path.exists('tree.json'):
			a=open('tree.json','w')
			a.close
			info=all_col('Nombre')
			for x in info:
				self.tree.insert(x)
			self.toJson()
		else:
			self.fromJson()


	def fromJson(self):
		with open('tree.json', 'r') as file:
			string=file.read()
		jsonData=json.loads(string)
		self.tree.root=self.__fromJson(jsonData)

	def __fromJson(self,json):
		if json==None:
			return None
		else:
			root=trees.treeNode(json["val"])
		if json["left"] != None:
			root.left=self.__fromJson(json["left"])
		if json["right"] != None:
			root.right=self.__fromJson(json["right"])
		self.tree.actualH(root)
		self.tree.size+=1
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
	def deletInf(self):
		self.tree=trees.avlTree('<U40')
		self.toJson()
		data = sqlite3.connect('tablas.db')
		cursor = data.cursor()
		cursor.execute('DELETE FROM productos')
		data.commit()
		Tabla()


	def deleteInf(self,name):
		if self.tree.delete(name):
			delet(name)
			self.toJson()
			return True
		return False

	def search(self,name):
		nombre= self.tree.search(self.tree.root,name)
		if nombre:
			return getRaw(nombre.val)
		else:
			return None

	def sortBy(self,column, first, last):
		if column=="fecha":
			return None
		else:
			toSort=all_col(column)
			index=list(range(self.tree.size))
			Sorted=trees.heapSort(toSort,self.tree.size,index)
			print(Sorted)
		data=get_all()
		print(data)
		temp=[]
		for i in Sorted[first:last]:
			print(i)
			producto=data[i]
			temp.append(producto)
		return temp

	def addInf(self,Nombre, precio, codigo, cantidad):
		if not self.search(Nombre):					#tener cuidado aqui
			
			insert(Nombre, precio, codigo, cantidad)
			self.tree.insert(Nombre)
			self.toJson()
			return True
		else:
			return False


a=almacen()

	
class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class linkedlist:
	def __init__(self):
		self.head = None
		self.tail = None
		self.cantidad = 0


	def add(self, newval):
		new_node = node(newval)
		if not self.head:
			self.head=new_node
		else:
			self.tail.next=new_node
		self.tail=new_node
		self.cantidad += 1

	def mostrar(self):
		printval = self.head
		while printval is not None:
			print(printval.data)
			printval = printval.next


"""class stack:
	def __init__(self):
		self.lista2 = linkedlist()

	def add2(self,value):
		#acá se define la cantidad maxima de elementos que puede tener el stack.
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
			return"""


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


class hashTable:
	def __init__(self,size):
		self.size=size
		self.array=np.array([linkedlist() for i in range(size)])

	def hashString(self,string):
		sol=0
		for char in string:
			sol+=ord(char)
		return (sol*15485863)%self.size

	def __setitem__(self,key,value):
		self.array[self.hashString(key)].add((key,value))

	def __getitem__(self,key):
		head=self.array[self.hashString(key)].head
		while head:
			if head.data[0]==key:
				return head.data[1]
			head=head.next
		return None


