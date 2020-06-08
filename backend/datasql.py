# Nombre, precio, codigo de barras, cantidad , fecha
import numpy as np
import os
import datetime
import sqlite3
import json
import numpy as np

data = sqlite3.connect('tablas.db')


def Tabla():
    cursor = data.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productos(
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        Nombre TEXT NOT NUll, 
        precio REAL, 
        codigo INTEGER, 
        cantidad INTEGER, 
        fecha DATETIME)"""
    )
    data.commit()

# a = string, b = float, c = int, d = int  (la fecha se pone automaticamente)
def insert(a, b, c, d):
    cursor = data.cursor()
    name =  (a,)
    cursor.execute('SELECT Nombre FROM productos')
    items = cursor.fetchall()
    if name not in items:
        entities = (a, b, c, d, datetime.date.today())
        cursor.execute('''INSERT INTO productos(Nombre, precio, codigo, cantidad, fecha) VALUES(?, ?, ?, ?, ?)''', entities)
        data.commit()
    else:
        print("el item ya existe")

def search(buscando):
    cursor = data.cursor()
    sentence = "SELECT * FROM productos WHERE Nombre LIKE ?;"
    cursor.execute(sentence, ["%{}%".format(buscando)])
    result = cursor.fetchall()
    result_list = []
    for i in result:
        result_list.append(i)
        print(i)
    if len(result_list) > 0:
        return result_list

def searchID(ID):
    cursor = data.cursor()
    sentence = "SELECT * FROM productos WHERE ID LIKE ?;"
    cursor.execute(sentence, ["%{}%".format(ID)])
    result = cursor.fetchall()
    result_list = []
    for i in result:
        result_list.append(i)
        print(i)
    if len(result_list) > 0:
        return result_list
    else:
        print("No se encuentra")

def get_all():
    cursor = data.cursor()
    cursor.execute('SELECT * FROM productos')
    filas = cursor.fetchall()
    temp = []
    with open('data.json', 'w') as file:
        for lista in filas:
            str = {"ID": lista[0],
                   "nombre": lista[1],
                   "precio": lista[2],
                   "codigo": lista[3],
                   "cantidad": lista[4],
                    "fecha": lista[5]}
            temp.append(str)
        json.dump(temp,file,indent=4)

def getAll(last, limit):
    data = sqlite3.connect('tablas.db')
    cursor = data.cursor()
    cursor.execute('SELECT * FROM productos WHERE ID > ? LIMIT ?;', (last, limit))
    filas = cursor.fetchall()
    temp2 = []
    with open('jall.json', 'w') as file:
        for lista in filas:
            str = {"ID": lista[0],
                   "nombre": lista[1],
                   "precio": lista[2],
                   "codigo": lista[3],
                   "cantidad": lista[4],
                    "fecha": lista[5]}
            temp2.append(str)
        json.dump(temp2,file,indent=4)



def delet(dell):
    cursor = data.cursor()
    cursor.execute('''DELETE FROM productos WHERE Nombre = ?''', (dell,))
    print("ok")
    data.commit()


def edit_c(nombre,cantidad):
    cursor = data.cursor()
    cursor.execute('''UPDATE productos SET cantidad = ? WHERE Nombre = ? ''', (cantidad, nombre))
    data.commit()


#esta función retorna un Nympy array
def all_col(columna):
    cursor = data.cursor()
    sentence = 'SELECT {} FROM productos'.format(columna)
    print(sentence)
    cursor.execute(sentence)
    col = cursor.fetchall()
    temp = []
    for i in col:
        temp.append(i[0])
    return np.array(temp)

def json_Conv(lista):
    json_string = "{nombre:lista[1] , precio:lista[2] , codigo:lista[3], cantidad: lista[4] , fecha: lista[5]}"
    with open('data.json', 'w') as file:
        file.write(json_string)


#retornar numpy array
# 1- introducir el nombre de las columna
# 2- Nombres: "Nombre", "precio", "codigo", "cantidad", "fecha"
# 3- respetar mayusculas y minusculas de los nombres de las columnas

""" 
Ejemplo 
    array = all_col("Nombre")
    print(array) 
    print(type(array)) -> numpy.array 
"""












