"""
escribir un programa que pida al usuario una palabra y muestre por consola
el n° de veces que contiene cada vocal
"""
#le pedimos al usuario ingresar una palabra
palabra = input("ingrese palabra:\n")
#vocales es un diccionario que permite contar las vocales en la palabra
vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

#recorre la palabra y cuanta el numero de vocales en esta 
for letra in palabra:
    if letra.lower() in vocales:
        vocales[letra.lower()] +=1

#muestra el resultado en consola 
print("la palabra '", palabra, "' contiene:")
for vocal, cantidad in vocales.items():
    print(cantidad, "ocurrencias de vocal", vocal)