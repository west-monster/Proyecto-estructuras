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
		remove("tablas.db")
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

	def sortBy(self,column):
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
		with open('jorg_'+column[0].lower()+'.json', 'w') as file:
			for i in Sorted:
				print(i)
				producto=data[i]
				temp.append(producto)
			json.dump(temp,file,indent=4)

	def addInf(self,Nombre, precio, codigo, cantidad):
		if not self.search(Nombre):					#tener cuidado aqui
			
			insert(Nombre, precio, codigo, cantidad)
			self.tree.insert(Nombre)
			self.toJson()
			return True
		else:
			return False


a=almacen()
a.addInf("m",2354,432,243)