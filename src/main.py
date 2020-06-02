import os
from os import system
from structures import *
from datasql import *
from time import time 
from datetime import date
import sys
import trees


if __name__ == '__main__':
    Tabla()


def loadTree():
	tree=avlTree('<U40')
	array=all_col("Nombre")
	for x in array:
		tree.insert(x)

	return tree

def sortBy(column):
	array=all_col(column)
	sort=trees.heapSort(array)

