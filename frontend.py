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
    
    t0 = time()
    for i in range(amnt):
        x = randomword(6)
        lista = [x,23,i,1,"12-02-12"]
        cargarObjeto(lista,"Default")
    
    tf = time()
    print("El tiempo para añadir ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 
def delete():
    amnt = int(input("Ingrese el numero de elementos a eliminar: "))
    a = almacenamiento()
    for i in range(amnt):
        x = randomword(6)
        lista = [x,23,i,1,"12-02-12"]
        a.add(lista)

    deleted = 0
    t0 = time()
    while deleted < amnt:
        a.delet(list(a.jisho.keys())[0])
        deleted +=1
    tf = time()

    print("El tiempo para eliminar ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 
def search():
    amnt = int(input("Ingrese el numero de elementos a buscar: "))
    a = almacenamiento()
    for i in range(amnt):
        x = randomword(6)
        lista = [x,23,i,1,"12-02-12"]
        a.add(lista)

    searched = 0
    t0 = time()
    while searched < amnt:
        a.search(list(a.jisho.keys())[0])
        searched +=1
    tf = time()

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
