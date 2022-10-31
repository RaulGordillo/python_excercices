"""
# Condicional if

Si se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecuta otro grupo de instrucciones
    
if condicion:
    instrucciones
else:
    Otras instrucciones
    
# operadores de comparación
== igual != diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

#Operadores lógicos:
and Y
or O  ! Negación
not NO

    
"""

# Ejemplo 1
print("############### EJEMPLO 1 ###################")

color = "rojo"

#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Felicidades !!")
    print("El color es ROJO")
else:
    print("Color incorrecto")

# Ejemplo 2
print("\n############### EJEMPLO 2 ###################")

year = 2020
#year = int(input("¿En qué año estamos?"))

if year < 2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior a 2021")

# Ejemplo 3
print("\n############### EJEMPLO 3 ###################")

nombre = "Raúl Gordillo"
ciudad = "Bogotá"
continente = "Europa"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "Suramérica":
        print("El usuario no es suramericano")
    else:
        print(f"{nombre} es suramericano y de la ciudad de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("\n############### EJEMPLO 4 ###################")

#dia = int(input("Ingrese el número del dia de la semana: "))
dia = 2

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miércoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

# Ejemplo 5
print("\n############### EJEMPLO 5 ###################")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 27

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("\n############### EJEMPLO 6 ###################")

pais = "Rusia"

if pais == "México" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")
    
# Ejemplo 7
print("\n############### EJEMPLO 7 ###################")
 
pais = "México"

if not (pais == "México" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana :(")
else:
    print(f"{pais} SI un pais de habla hispana :)")
    
# Ejemplo 8
print("\n############### EJEMPLO 8 ###################")
 
pais = "USA"

if pais != "México" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana :(")
else:
    print(f"{pais} SI un pais de habla hispana :)")

