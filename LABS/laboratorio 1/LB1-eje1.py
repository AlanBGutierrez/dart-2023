"""
Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y se debe
añadir uno por uno los elementos de ambas matrices. Luego se deben sumar estas matrices
en una función, y en otra función restarlas. Solo utilizando las funciones de la biblioteca
numpy.
"""
import numpy as np 
f1=int(input("ingrese filas para la matriz uno:\n"))
c1=int(input("ingrese columnas para la matriz uno:\n"))
matriz1=np.zeros((f1,c1))
print("ingrese elementos para la primera matriz:\n")
for i in range(f1):
    for j in range(c1):
        matriz1[i][j]=float(input())

f2=int(input("ingrese filas para la matriz dos:\n"))
c2=int(input("ingrese columnas para la matriz dos:\n"))
matriz2=np.zeros((f2,c2))
print("ingrese elementos para la primera matriz:\n")
for i in range(f2):
    for j in range(c2):
        matriz2[i][j]=float(input())
suma=np.add(matriz1, matriz2)
print(suma)
resta=np.


        

    