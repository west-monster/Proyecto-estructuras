import numpy as np
from estructuras import almacenamiento
import pickle

def crearSesion(nombre):

	objeto=almacenamiento()
	archivo=open(nombre+".pickle","wb")
	pickle.dump(objeto,	archivo)
	archivo.close()

def cargarSesion(nombre):

	archivo=open(nombre+".pickle","rb")
	almacen=pickle.load(archivo)
	archivo.close()
	return almacen

def guardarSesion(nombre, almacen):

	archivo=open(nombre+".pickle","wb")
	pickle.dump(almacen,archivo)
	archivo.close()
