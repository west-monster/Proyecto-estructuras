import os
from os import system
from estructuras import *
from pickles import *
from time import time 
from datetime import date
from prettytable import PrettyTable

def option():
    while True:
        menuElements = ["Menú principal","- m ----- Mostrar todo", "- l ----- Añadir","- a ----- Añadir data Auto", "- g ----- Guardar",
         "- b ----- Buscar", "- d ----- Eliminar todo", "- e ----- Eliminar" , "- q ----- Salir"]
        #Print menu with format
        print(menuElements[0].center(os.get_terminal_size().columns,'-'),  end = '')

        for x in range(1, len(menuElements)):
            print(menuElements[x].ljust(27).center(os.get_terminal_size().columns),  end = '')
            
        print(''.center(os.get_terminal_size().columns,'-'))

        answer = input()

        if answer == "m":
            print("Ok")
            show()
        if answer == "l":
            load()
        elif answer == "a": 
            loadDataAuto()
        elif answer == "b":
            search()
        elif answer == "d":
            deleteEverything() 
        elif answer == "e":
            delete()
        elif answer == "DEV":
            if len(answer.split()) > 1:
                if answer.split()[1] == "--help":
                    print("-l agregar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("-d eliminar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("-s buscar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
                    _ = input()
                    _ = system('cls')
                elif answer.split()[1] == "-l":
                    massiveLoad()
                elif answer.split()[1] == "-d":
                    massiveDelete()
                elif answer.split()[1] == "-s":
                    masiveSearch()
                else:
                    print("Valor incorrecto, --help para ver opciones".center(os.get_terminal_size().columns,' '))
            else:
                print("Parametro esperado".center(os.get_terminal_size().columns,' '))  
                print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
                _ = input()
                _ = system('cls') 
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

def show():
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for index in range(0,almacen.size):
        if almacen.data[index] != 0:
            t.add_row(almacen.data[index])
    print(t)

    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')

def load():
    amnt = int(input("Ingrese el numero de elementos a cargar: "))
    almacen=cargarSesion("Default")
    for i in range(amnt):
        lista=[]
      
        lista.append(input("Ingrese nombre: "))
        lista.append(float(input("Ingrese precio: ")))
        lista.append(int(input("Ingrese codigo de barras: ")))
        lista.append(int(input("Ingrese cantidad: ")))

        lista.append(date.today())
        #x = randomword(6)
        #lista = [x,23,i,1,"03-08-1917"] #usar para pruebas random
        almacen.add(lista)
    guardarSesion("Default", almacen)
    print("Elementos añadidos")
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 

def delete():
    amnt = int(input("Ingrese el numero de elementos a eliminar: "))

    almacen=cargarSesion("Default")

    for _ in range(amnt):
        toDelete = input("Ingrese nombre de objeto a eliminar: ")
        almacen.delet(toDelete)

    guardarSesion("Default", almacen)

    print("El tiempo para eliminados")
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')  

def search():
    amnt = int(input("Ingrese el numero de elementos a buscar: "))
    almacen=cargarSesion("Default")
    searched = 0
    while searched < amnt:
        toSearch = input()
        elmt = almacen.search(toSearch)
        searched +=1
        if elmt != None:
            printElement(elmt,almacen)

    guardarSesion("Default", almacen)
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 

def massiveLoad():
    _ = system('cls')
    amnt = int(input("Ingrese el numero de elementos a cargar: "))
    almacen=cargarSesion("Default")
    t0 = time()
    for i in range(amnt):
        x = randomword(6)
        lista = [x,23,i,1,"12-02-12"]
        almacen.add(lista)
    guardarSesion("Default", almacen)
    tf = time()
    print("El tiempo para añadir ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')

def massiveDelete():
    amnt = int(input("Ingrese el numero de elementos a eliminar: "))
    almacen=cargarSesion("Default")
    for i in range(amnt):
        x = randomword(6)
        lista = [x,23,i,1,"03-08-1917"]
        almacen.add(lista)
    guardarSesion("Default", almacen)
    deleted = 0
    t0 = time()
    while deleted < amnt:
        almacen.delet(list(almacen.dictNames.keys())[0])
        deleted +=1
    guardarSesion("Default", almacen)
    tf = time()

    print("El tiempo para eliminar ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')

def masiveSearch():
    amnt = int(input("Ingrese el numero de elementos a buscar: "))
    almacen=cargarSesion("Default")
    for i in range(amnt):
        x = randomword(6)
        lista = [x,23,i,1,"03-08-1917"]
        almacen.add(lista)
    guardarSesion("Default", almacen)
    searched = 0
    t0 = time()
    while searched < amnt:
        almacen.search(list(almacen.dictNames.keys())[0])
        searched +=1
    guardarSesion("Default", almacen)
    tf = time()

    print("El tiempo para buscar ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')

def loadDataAuto():
    _ = system('cls')
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for x in almacen.dictNames:
        if almacen.data[int(almacen.dictNames.get(x))] != 0:
            t.add_row(almacen.data[int(almacen.dictNames.get(x))])
    print(t)
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')

def deleteEverything():
    almacen=cargarSesion("Default") 
    almacen.data = np.zeros((50,) ,dtype=object)
    almacen.capacity = 50
    almacen.size = 0
    almacen.references = 1
    almacen.freeSpace = []
    almacen.dictNames = {"nombre": 0}
    guardarSesion("Default", almacen)
    print("Datos eliminados".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls')

def printElement(index, almacen):
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    if almacen.data[index] != 0:
        t.add_row(almacen.data[index])
    print(t)

if __name__ == '__main__':
    if not os.path.exists("Default.pickle"):
        crearSesion("Default")
    option()

			
