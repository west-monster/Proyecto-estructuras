from tarea import almacenamiento
import pickle

def crearSesion(nombre):

	objeto=almacenamiento()
	archivo=open(nombre+".pickle","wb")
	pickle.dump(objeto,	archivo)
	archivo.close()

def cargarObjeto(datosLista,nombreSesion):
	
	archivo=open(nombreSesion+".pickle","rb")
	almacen=pickle.load(archivo)
	almacen.add(datosLista)
	archivo.close()

	archivo=open(nombreSesion+".pickle","wb")
	pickle.dump(almacen,archivo)
	archivo.close()


def borrarObjeto(nombreObjeto,nombreSesion):
	
	archivo=open(nombreSesion+".pickle","rb")
	almacen=pickle.load(archivo)
	almacen.delet(nombreObjeto)
	archivo.close()

	archivo=open(nombreSesion+".pickle","wb")
	pickle.dump(almacen,archivo)
	archivo.close()

def buscarObjeto(nombreObjeto,nombreSesion):
	
	archivo=open(nombreSesion+".pickle","rb")
	almacen=pickle.load(archivo)
	archivo.close()
	return almacen.searcher(nombreObjeto)
