#Practico 6: Estructuras de datos complejas

"""Actividad 1:
Dado el diccionario precios_frutas

Añadir las siguientes frutas con sus respectivos precios:

    * Naranja = 1200
    * Manzana = 1500
    * Pera = 2300
    
    Actividad 2:
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior
actualizar los precios de las siguientes frutas:

    * Banana = 1330
    * Manzana = 1700
    * Melón = 2800
    
    Actividad 3:
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior
crear una lista que contenga únicamente las frutas sin los precios."""

print("##### Precios de Nuestras Frutas #####")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("##### Precios de Nuestras Frutas #####")
print(precios_frutas)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("##### Precios de Nuestras Frutas #####")
print(precios_frutas)

print("##### Nuestra lista de frutas #####")
lista_frutas = list(precios_frutas)

print(lista_frutas)

"""Actividad 4

Escribí un programa que permita almacenar y consultar números telefónicos
    * Permití al usuario cargar 5 contactos con su nombre como clave y número como valor
    * Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

contactos = {}

print("##### Contactos #####")

for i in range(5):
    print(f"Contacto : {i + 1}: ")
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingresa el número de teléfono: ")

    contactos[nombre] = telefono

nombreBuscar = input("Ingresa el nombre que deseas buscar: ")

encontradoContacto = contactos.get(nombreBuscar)

if encontradoContacto:
    print(f"El número de {nombreBuscar} es : {encontradoContacto}.")
else:
    print(f"El contacto {nombreBuscar} no corresponde a un abonado en servicio.")
"""
Actividad 5
Solicita al usuario una frase e imprime:
    * Las palabras únicas (usando un set).
    * Un diccionario con la cantidad de veces que aparece cada palabra.
"""

frase = input("Ingresá una frase: ")

palabras = frase.split() #convierte la frase en lista de palabras

palabras_unicas = set(palabras) #con esto se elimina los duplicados

guardado = {}

for palabra in palabras:
    if palabra in guardado:
        guardado[palabra] += 1
    else:
        guardado[palabra] = 1

print(f"Palabras {palabras_unicas}")
print(f"Lo que hemos guardado {guardado}")

"""Actividad 6
Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas
Luego, mostrá el promedio de cada alumno."""

nombre_estudiante = {}

print("#### Ingrese las notas de los estudiantes ####")

for i in range(3):
    print(f"Estudiante {i + 1}: ")
    nombre = input("Ingrese el nombre del estudiante: ")

    nota1 = int(input("Ingrese la nota 1: "))
    nota2 = int(input("Ingrese la nota 2: "))
    nota3 = int(input("Ingrese la nota 3: "))

    #tupla
    tupla_notas = (nota1, nota2, nota3)

    nombre_estudiante[nombre] = tupla_notas

print ("#### El promedio de los estudiantes ####")

for nombre, notas in nombre_estudiante.items():
    promedio = sum(notas) / len(notas)

    print(f"El promedio de {nombre} es : {promedio:.2f}")
"""
Actividad 7
Dado dos sets de números, representando dos listas de estudiantes que aprobaron parcial 1
y parcial 2:
    * Mostrá los que aprobaron ambos parciales
    * Mostrá los que aprobaron solo uno de los dos
    * Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
"""

parcial1 = {1, 2, 3, 4, 5, 6, 7, 8}
parcial2 = {1, 3, 4, 6, 8, 9, 10}

print("Los estudiantes que aprobar el primer parcial fueron ", parcial1)
print("Los estudiantes que aprobaron el segundo parcial fueron ", parcial2)

ambosParciales = parcial1 & parcial2
print("Aquellos que aprobaron los dos parciales: ", ambosParciales)

unParcial = parcial1 ^ parcial2
print("Quienes solo aprobaron un solo parcial: ", unParcial)

totalUno = parcial1 | parcial2
print("Quienes aprobaron AL MENOS UN parcial: ",totalUno)

"""Actividad 8
Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
    * Consultar el stock de un producto ingresado.
    * Agregar unidades al stock si el producto ya existe
    * Agregar un nuevo producto si no existe"""

inventario = {
    "procesador ryzen": 10,
    "memoria ram ddr4": 24,
    "placa de video rtx": 5
}

print("#### Stock de productos ####")

producto = input("Ingresa el nombre del producto a consultar/agregar: ").lower()

if producto in inventario:
    print(f"El producto '{producto}' ya existe. Stock actual: {inventario[producto]} unidades.")

    unidades = int(input(f"Deseas agregar unidades a {producto} ? "))
    inventario[producto] += unidades

    print(f"El nuevo stock de {producto} es {inventario[producto]}")

else:
    print(f"El prodcuto {producto} NO se registra en el inventario.")
    unidades = int(input(f"Ingresa el stock del nuevo producto {producto}"))

    inventario[producto] = unidades
    print(f"Se agregó exitosamente {producto} con su stock de {unidades}")

print("#### Actualización de STOCK ####")
print(inventario)

"""Actividad 9
Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
"""

agenda = {
    ("lunes", "08:00"): "Clases de Organización Empresarial",
    ("martes", "08:00"): "Clases de Programación 1",
    ("Miércoles", "08:00"): "Clases de Arquitectura y Sistemas Operativos",
    ("Jueves", "15:00"): "Gimnasio",
    ("Viernes", "16:00"): "Gimnasio + Cardio"
}

print("#### Su agenda ####")

dia = input("Ingresá el día a consultar. ").lower()
hora = input("Ingresá la hora que deseas consultar - ejemplo 10:00 - : ")

consultar = (dia, hora)

if consultar in agenda:
    print(f"La {hora} del día {dia} tenes programada {agenda[consultar]}")
else:
    print("No hay actividad para dicha fecha u hora.")

"""Actividad 10
Dado un diccionario que mapea nombres de paises con sus capitales, construí un nuevo diccionario
donde:
    * Las capitales sean las claves
    * Los países sean los valores
"""

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Brasil": "Brasilia"
}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario Original: ", original)
print("Diccionario Invertido: ", invertido)