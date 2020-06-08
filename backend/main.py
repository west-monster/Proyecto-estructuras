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
			return self.tree.printTree()
		elif column=="fecha":
			return None
		else:
			toSort=all_col(column)
			
			return trees.heapSort(toSort,self.tree.size)
		

a=almacen()

print(a.sortBy("ID"))
