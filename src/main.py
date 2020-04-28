import os
from os import system
from structures import *
from pickles import *
from time import time 
from datetime import date
import sys
sys.path.insert(1, '../lib/prettytable-0.7.2')
from  prettytable import PrettyTable

def option():
    while True:
        menuElements = ["Menú principal","- m ----- Mostrar todo", "- l ----- Añadir","- a ----- Añadir data Auto", "- g ----- Guardar",
         "- b ----- Buscar","- o ----- Ordenar alfabeticamente", "- d ----- Eliminar todo", "- e ----- Eliminar" , "- q ----- Salir"]
        #Print menu with format
        print(menuElements[0].center(os.get_terminal_size().columns,'-'),  end = '')

        for x in range(1, len(menuElements)):
            print(menuElements[x].ljust(33).center(os.get_terminal_size().columns),  end = '')
            
        print(''.center(os.get_terminal_size().columns,'-'))

        answer = input()

        if answer == "m":
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

        elif answer == "o":
            showSort()
        elif len(answer) > 0 and answer.split()[0] == "DEV":
            if len(answer.split()) > 1:
                if answer.split()[1] == "--help":
                    print("-l agregar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("-d eliminar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("-s buscar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
                    _ = input()
                    os.system('clear')
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
                os.system('clear')
        elif answer == "q":
            os.system('clear')
            print("Hasta pronto".center(os.get_terminal_size().columns,'*'))
            return False

        else:
            os.system('clear')
            print("La opcion es incorrecta, ingresela de nuevo")

def notDefined():
    os.system('clear')
    print("Lo sentimos, esta utilidad estará disponible en futuras versiones.".center(os.get_terminal_size().columns))
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    os.system('clear')

def show():
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for index in range(0,almacen.size):
        if almacen.data[index] != 0:
            t.add_row(almacen.data[index])
    print(t)

    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    os.system('clear')

def load():
    amnt = int(input("Ingrese el numero de elementos a cargar: "))
    almacen=cargarSesion("Default")
    t0=time()
    for i in range(amnt):
        lista=[]
      
        lista.append(input("Ingrese nombre: "))
        lista.append(float(input("Ingrese precio: ")))
        lista.append(int(input("Ingrese codigo de barras: ")))
        lista.append(int(input("Ingrese cantidad: ")))

        lista.append(date.today())
        #x = randomword(6)
        #lista = [x,23,i,1,"12-02-12"] #usar para pruebas random
        almacen.add(lista)
    guardarSesion("Default",almacen)
    print("Elementos añadidos")	

    

    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    os.system('clear')

def delete():
    amnt = int(input("Ingrese el numero de elementos a eliminar: "))

    almacen=cargarSesion("Default")

    for _ in range(amnt):
        toDelete = input("Ingrese nombre de objeto a eliminar: ")
        almacen.delet(toDelete)
    guardarSesion("Default",almacen)
    print("Elemento eliminado")
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    os.system('clear')

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
    os.system('clear')

def massiveLoad():
    os.system('clear')
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
    os.system('clear')

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
    os.system('clear')

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
    guardarSesion("Default", almacen)

    print("El tiempo para buscar ", amnt, " elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    os.system('clear')

def loadDataAuto():
    os.system('clear')
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for x in almacen.dictNames:
        if almacen.data[int(almacen.dictNames.get(x))] != 0:
            t.add_row(almacen.data[int(almacen.dictNames.get(x))])
    print(t)
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    os.system('clear')

def deleteEverything():
    os.remove("../data/Default.pickle")
    crearSesion("Default")

    print("Datos eliminados".center(os.get_terminal_size().columns))
    _ = input()
    os.system('clear')

def printElement(index, almacen):
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    if almacen.data[index] != 0:
        t.add_row(almacen.data[index])
    print(t)

def showSort():
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for x in almacen.bSort():
        t.add_row(almacen.data[int(almacen.dictNames.get(x))])
    print(t)


if __name__ == '__main__':
    if not os.path.exists("../data/Default.pickle"):
        crearSesion("Default")
    
    option()

			
