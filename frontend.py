import os
from os import system
from estructuras import *
from pickles import *
from time import time 
def option():
    while True:
        menuElements = ["Menú principal", "- l ----- Añadir","- c ----- Crear categoria", "- a ----- Cargar data Auto", "- m ----- Cargar data manual",
         "- b ----- Buscar", "- f ----- Filtrar", "- d ----- Eliminar todo", "- e ----- Eliminar" , "- q ----- Salir"]
        #Print menu with format
        print(menuElements[0].center(os.get_terminal_size().columns,'-'),  end = '')

        for x in range(1, len(menuElements)):
            print(menuElements[x].ljust(27).center(os.get_terminal_size().columns),  end = '')
            
        print(''.center(os.get_terminal_size().columns,'-'))

        answer = input() 
        if answer == 'l':
            load()
        elif answer == "c":
            createCategory()
        elif answer == "a": 
            loadDataAuto()  
        elif answer == "m":
            loadDataManual()  
        elif answer == "b":
            search()  
        elif answer == "f":
            filterMenu()
        elif answer == "d":
            deleteEverything()  
        elif answer == "e":
            delete()
        elif answer == "q":
            _ = system('cls') 
            print("Hasta pronto".center(os.get_terminal_size().columns,'*'))
            return False

        else:
            _ = system('cls') 
            print("La opcion es incorrecta, ingresela de nuevo")
def notDefined():
    _ = system('cls') 
    print("Lo sentimos, esta utilidad estará disponible en futuras versiones.".center(os.get_terminal_size().columns))
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 
def load():
    amnt = int(input("Ingrese el numero de elementos a cargar: "))
    
    almacen=cargarSesion("Default")
    t0 = time()
    for i in range(amnt):
        lista=[]
      
        lista.append(input("Ingrese nombre: "))
        lista.append(int(input("Ingrese precio: ")))
        lista.append(int(input("Ingrese codigo de barras: ")))
        lista.append(int(input("Ingrese cantidad: ")))

        lista.append("{}/{}/{}".format(today.day,today.month,today.year))
        #x = randomword(6)
        #lista = [x,23,i,1,"12-02-12"] #usar para pruebas random
        almacen.add(almacen,lista)
    guardarSesion("Default")
    tf = time()
    print("El tiempo para añadir ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 

def delete():
    amnt = int(input("Ingrese el numero de elementos a eliminar: "))

    almacen=cargarSesion("Default")

    for _ in range(amnt):
        almacen.delete("Ingrese nombre de objeto a eliminar: ")

    guardarSesion(almacen,"Default")

    print("El tiempo para eliminar ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')  
def search():
    amnt = int(input("Ingrese el numero de elementos a buscar: "))
    almacen=cargarSesion("Default")

    searched = 0
    t0 = time()
    while searched < amnt:
        almacen.search("Ingrese nombre de objeto a buscar: ")
        searched +=1
    tf = time()
    guardarSesion(almacen,"Default")
    print("El tiempo para buscar ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 
def createCategory():
    notDefined()
def loadDataAuto():
    notDefined()
def loadDataManual():
    notDefined()
def filterMenu():
    notDefined()
def deleteEverything():
    notDefined()    

if __name__ == '__main__':
    if not os.path.exists("Default.pickle"):
        crearSesion("Default")
    option()
