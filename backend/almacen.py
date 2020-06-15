
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

#for x in range(10000):
#	insert(randomword(4),3.36,4,5)

#a.sortBy("Nombre")

	