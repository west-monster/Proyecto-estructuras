import os
from os import system
from structures import *
from datasql import *
from time import time 
from datetime import date
import sys
import trees
import json
import numpy as np

if __name__ == '__main__':
    Tabla()


    
class almacen():
	"""docstring for almacen"""
	def __init__(self):
		info=all_col('nombre')
		self.tree=trees.avlTree('<U40')
		for x in info:
			self.tree.insert(x)


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
			json.dump(temp,file,indent=4)

a=almacen()

#for x in range(10000):
#	insert(randomword(4),3.36,4,5)

a.sortBy("Nombre")

	