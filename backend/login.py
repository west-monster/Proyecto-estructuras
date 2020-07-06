import json
from os import path
from structures import randomword
class hashTable:
	def __init__(self,size):
		self.size=size
		self.array=[[] for i in range(size)]

	def hashString(self,string):
		sol=0
		for i in range(len(string)):
			sol+=ord(string[i])*i+1
		return (sol*15485863)%self.size
	def __setitem__(self,key,value):
		lista=self.array[self.hashString(key)]
		for i in range(len(lista)):
			if lista[i][0]==key:
				lista[i]=(key,value)
				return True
		lista.append((key,value))

	def __getitem__(self,key):
		lista=self.array[self.hashString(key)]
		for i in range(len(lista)):
			if lista[i][0]==key:
				return lista[i][1]

	def delete(self,key):
		lista=self.array[self.hashString(key)]
		for i in range(len(lista)):
			if lista[i][0]==key:
				lista.pop(i)
				return True
		return False

	def fromJson(self):
		with open('user.json', 'r') as file:
			string=file.read()
			print(string)
		self.array=json.loads(string)
		self.size=len(self.array)

	def toJson(self):
		with open('user.json', 'w') as file:
			json.dump(self.array,file,indent=4)

def getTable():
	if not path.exists('user.json'):
		file=open('user.json','w')
		file.close
		table=hashTable(200)

	else:
		table=hashTable(1)
		table.fromJson()
	return table

def crearUsuario(user,password):	
	table=getTable()
	table[password]=user
	table.toJson()

def validarLogin(user,password):
	table=getTable()
	return table[password]==user

