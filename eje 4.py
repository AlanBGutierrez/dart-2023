""""
crear arreglo aleatorio de tamaño entre 10 a 30 [10;30]
imprimir el arreglo creado y luego solicitar por consola la 
busqueda de un elemento en especifico del arreglo creado 
todo esto utilizando array 
"""
import random

from array import array

# Generar un número aleatorio entre 10 y 30 para determinar el tamaño del arreglo
tamaño = random.randint(10, 30)

# Crear un arreglo vacío con el tamaño generado aleatoriamente
arreglo = array('i', [0] * tamaño)

# Llenar el arreglo con números aleatorios entre 0 y 30
for i in range(tamaño):
  arreglo[i] = random.randint(0, 30)

# Imprimir el arreglo generado
print(arreglo)

# Solicitar al usuario un número a buscar en el arreglo
numero_buscar = input("Ingrese un número a buscar en el arreglo: ")

# Convertir la entrada del usuario a un número entero
try:
  numero_entero = int(numero_buscar)

  # Buscar el número en el arreglo
  indice = arreglo.index(numero_entero)

  # Imprimir el resultado de la búsqueda
  print(f"El número {numero_entero} fue encontrado en el índice {indice} del arreglo.")
except ValueError:
  # La entrada del usuario no es un número válido o el número no está en el arreglo
  print(f"El número {numero_buscar} no fue encontrado en el arreglo o no es un número válido.")