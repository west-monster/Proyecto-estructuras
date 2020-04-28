import numpy as np
from structures import almacenamiento
import pickle

def crearSesion(nombre):

	objeto=almacenamiento()
	archivo=open("../data/"+nombre+".pickle","wb")
	pickle.dump(objeto,	archivo)
	archivo.close()

def cargarSesion(nombre):

	archivo=open("../data/"+nombre+".pickle","rb")
	almacen=pickle.load(archivo)
	archivo.close()
	return almacen

def guardarSesion(nombre, almacen):

	archivo=open("../data/"+nombre+".pickle","wb")
	pickle.dump(almacen,archivo)
	archivo.close()
