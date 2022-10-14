# Tipos de datos

from numpy import byte


nada = None
cadena = "Hola soy Raúl Gordillo WEB"
entero = 5
decimal = 5.63
booleano = False
lista = [10, 20, 30, 100, 200, 300, 400]
listaString = [44, "treinta", 30, "cuarenta", 85.5]
tupla = ("Máster", "en", "python")
diccionario = {"nombre": "Raúl",
               "apellido": "Gordillo",
               "curso": "Máster en python"
               }
rango = range(9)
dato_byte = b"Probando"

# imprimir variable
print(nada)
print(cadena)
print(entero)
print(decimal)
print("------------------")

# mostrar tipo de dato de una variable
print(f"el dato es: {nada}", "-", type(nada))
print(f"la cadena es: {cadena}", "-", type(cadena))
print(f"el número es: {entero}", "-", type(entero))
print(f"el número es: {decimal}", "-", type(decimal))
print(f"el boolenano es: {booleano}", "-", type(booleano))
print(f"la lista es: {lista}", "-", type(lista))
print(f"la lista variada es: {listaString}", "-", type(listaString))
print(f"la tupla es: {tupla}", "-", type(tupla))
print(f"el diccionario es: {diccionario}", "-", type(diccionario))
print(f"el rango es: {rango}", "-", type(rango))
print(f"el tipo byte es: {dato_byte}", "-", type(dato_byte))

#Convertir datos
print("----------------")
texto ="Hola soy un texto"
numerito = str(776)
print(type(numerito))
print (texto + " " + numerito)

numerito = int(776)
print(type(numerito))

numerito = float(776)
print(numerito)
