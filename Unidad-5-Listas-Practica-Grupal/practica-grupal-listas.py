#import numpy as np

#Ejercicio 1: Suma de Elementos

listaUno = []

while True:
    ingresoUno = input("Ingresa un número (o terminar para cerrar el programa): ")

    if ingresoUno.lower() == "terminar":
        break

    numero = int(ingresoUno)
    listaUno.append(numero)

suma = sum(listaUno)
print(f"La sumatoria total es {suma}")

#Ejercicio 2: Encontrar el Mayor y el Menor

listaDos = []

while True:
    ingresoDos = input("Ingresa una lista de números, o usa la palabra terminar para cortar el programa: ")

    if ingresoDos.lower() == "terminar":
        break
    listaDos.append(int(ingresoDos))

if listaDos:
    mayor = max(listaDos)
    menor = min(listaDos)
    print(f"El mayor {mayor} y el menor {menor}")
else:
    print("No ingresaste datos.")

#Ejercicio 3: Invertir una lista

listaTres = []

while True:
    ingresoTres = input("Ingresa una lista de números para invertirla, si deseas salir usa la palabra terminar: ")

    if ingresoTres.lower() == "terminar":
        break

    listaTres.append(int(ingresoTres))

listaTres.reverse()

print(f"Y su lista queda así : {listaTres}")

#Ejercicio 4 : Contar Elementos Pares e Impares

listaCuatro = []

while True:
    ingresoCuatro = input("Ingresa una lista, misma forma para salir: ")

    if ingresoCuatro.lower() == "terminar":
        break

    listaCuatro.append(int(ingresoCuatro))

pares = [i for i in listaCuatro if i % 2 == 0]
impares = [i for i in listaCuatro if i % 3 == 0]

print(f"Números pares {pares}")
print(f"Números impares {impares}")

#Ejercicio 5 : Multiplicar Elementos por un valor

listaCinco = [2,3,5,8,10,4]
print(f"Esta es la lista predefinida por la cuál se multiplicará por el usuario {listaCinco}")

multiplicar = int(input("Ingresa el número con el cuál multiplicaras la lista predefinida: "))

listaMultiplicada = []
for numero in listaCinco:
    listaMultiplicada.append(numero * multiplicar)

print(f"Esta es la nueva lista multiplicada {listaMultiplicada}")

#Ejercicio 6 : Eliminar Duplicados

listaSeis = []

while True:
    ingresoSeis = input("Ingresa varios números aleatorios y verás que sucede. (Palabra para cortar el programa - terminar -)")

    if ingresoSeis.lower() == "terminar":
        break

    listaSeis.append(int(ingresoSeis))

listaSinDuplicados = set(listaSeis)

print(f"Esta es la lista que creaste {listaSeis} para eliminar ahora los duplicados.")
print(f"Y esta es la nueva lista sin duplicados : {listaSinDuplicados}")

#Ejercicio 7 : Promedio de una lista

listaSiete = []

while True:
    ingresoSiete = input("Ingresa distintos números para hacer un promedio. Misma ejecución de cierre.")

    if ingresoSiete.lower() == "terminar":
        break

    listaSiete.append(int(ingresoSiete))

print(f"La lista que me diste es esta {listaSiete}")

cantidadSiete = len(listaSiete)
sumaSiete = sum(listaSiete)
promedioSiete = sumaSiete / cantidadSiete

print(f"El promedio de la lista fue {promedioSiete}")

#Ejercicio 8 : Encontrar elementos Repetidos

listaOcho = [2,2,4,5,7,2,9,12,10,1,1,0,6,8,11]

print(f"Aquí la lista en la cual muestre los elementos repetidos {listaOcho}")

leidos = set()
repetidos = set()

for numero in listaOcho:
    if numero in leidos:
        repetidos.add(numero)
    else:
        leidos.add(numero)

print(f"Los elementos repetidos : {repetidos}")

#Ejercicio 9 : Lista de Números primos

listaNueve = []

while True:
    ingresoNueve = input("Ingrese distintos números para buscar sus números primos, para salir escriba : terminar.")

    if ingresoNueve.lower() == "terminar":
        break

    listaNueve.append(int(ingresoNueve))

numerosPrimos = []

for numero in listaNueve:
    if numero <= 1:
        continue

    es_primo = True

    for divisor in range(2, numero): #ya que los números menores o iguales a 1 NO son primos
        if numero % divisor == 0:
            es_primo = False
            break

    if es_primo:
        numerosPrimos.append(numero)

print(f"Los números primos encontrados son {numerosPrimos}")

#Ejercicio 10 : Eliminar un elemento por su índice

listaDiez = []

while True:
    ingresoDiez = input("Ingresa distintos números para crear uina lista, si deseas salir escriba : terminar.")

    if ingresoDiez.lower() == "terminar":
        break

    listaDiez.append(int(ingresoDiez))

print(f"Esta es la lista que haz creado : {listaDiez}")

eliminarIndice = int(input("Que indice deseas eliminar?: "))

if eliminarIndice >= 0 and eliminarIndice < len(listaDiez):
    elemento = listaDiez[eliminarIndice]

    del listaDiez[eliminarIndice]

    print(f"Se eliminó {elemento} y ahora tu nueva lista es : {listaDiez}")

#Ejercicio 11 : Contar Ocurrencias de un elemento

listaOnce = []

while True:
    ingresoOnce = input("Ingresa una lista y esta te dirá cuantas veces aparece un número X, usa la palabra TERMINAR para acabar el programa: ")

    if ingresoOnce.lower() == "terminar":
        break

    listaOnce.append(int(ingresoOnce))

print(f"Tu lista creada {listaOnce}")

buscarNumero = int(input("Qué número deseas contabilizar?"))

contador = 0

for elemento in listaOnce:
    if elemento == buscarNumero:
        contador = contador + 1

print(f"El número que quisiste contabilizar {buscarNumero} aparece {contador} veces.")

#Ejercicio 12 : Sumar Listas elemetno por elemento

listaDocePar = [2,4,6,8,10]
listaDoceImpar = [1,3,5,7,9]

if len(listaDocePar) == len(listaDoceImpar):
    listaSumar = []

    for i in range(len(listaDocePar)):
        sumar = listaDocePar[i] + listaDoceImpar[i]
        listaSumar.append(sumar)

    print(f"Esta es la sumatoria de la lista {listaSumar}")

    for i in range(len(listaDocePar)):
        print(f"{listaDocePar[i]} + {listaDoceImpar[i]} = {listaSumar[i]}")

#Ejercicio 13 : Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays

"""La librería NumPy está pensada para el cálculo numérico que ofrece un rendimiento mayor a las listas nativas
de Python, esto permitiendo trabajar mejor las matrices. 
Introduce los arrays, que son estructuras de datos homogéneas (mismo tipo de datos).
Uno de los beneficios es el quitar la necesidad de usar bucles "for"


Ejemplo sacado de DeepSeek

vector = np.array([1, 2, 3, 4])
print(vector)

#crea matriz 2D

matriz = np.array([[1, 2, 3],
                   [4, 5, 7],
                   [7, 8, 9]])
print(matriz)"""