# Una variable es un contenedor de información que dentro guardar´pa un dato, se puede crear muchas variables y que cada una tenga un dato distinto


# Crear variables y asignarles un valor
texto = "Máster en python"
texto2 = "con Raúl Gordillo"
numero = 45
decimal = 6.7

# Mostrar valor de los valores
print(texto)
print(texto2)
print(numero)
print(decimal)

print("----------------------------")

# Sustitir variables
numero = 77
decimal = 8.9

print(numero)
print(decimal)
print("----------------------------")

# Concatenación
nombre = "Raúl"
apellidos = "Gordillo"
web = "zabaleta.inc"

print(nombre + " " + apellidos + "-" + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

# Este printo no contatena
print(nombre, apellidos, web)
