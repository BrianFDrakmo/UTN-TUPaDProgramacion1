import random

#Actividad 1
#Crear un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Ahora saldrá por pantalla todos los números enteros desde 0 hasta 100, incluyendolos.")
print("-" * 30)

for i in range(0, 101, 1):
    print(i, end=" ")

print("\n")

#Actividad 2
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

print("-" * 30)

numEntero = int(input("Ingrese un número así se determina la cantidad de dígitos que tiene: "))
numUsuario1 = numEntero #Almaceno el numero original para poder mostrarlo por terminal

contadorEntero = 0

if numEntero == 0:
    print("El 0 (cero) tiene 1 dígito.")
else:
    numEntero = abs(numEntero) #Esto por si el usuario usa un número negativo
    
    while numEntero > 0:
        numEntero = numEntero // 10
        contadorEntero += 1

    print(f"El total de dígitos de {numUsuario1} es : {contadorEntero}")

#Actividad 3
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario
#excluyendo esos dos valores.

print("-" * 30)

print("Ahora se hará una sumatoria total de todos los números comprendidos entre dos valores que el Usuario dará.")
numeroUno = int(input("Escribe el 1re número entero: "))
numeroDos = int(input("Escribe el 2do número entero: "))

suma = 0 #creamos contador para almacenar la sumatoria del bucle for
if numeroUno < numeroDos: #para poder ordenar de menor a mayor los números
    for total in range(numeroUno + 1, numeroDos):
        suma = suma + total

else: 
    for total in range(numeroUno - 1, numeroDos, -1):
        suma = suma + total

print(f"La sumatoria de todos los números entre {numeroUno} + {numeroDos} = {suma}")

#Actividad 4
#Elaborar un programa que permita al usuario ingresar números enteros y los sume en secuencia.
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("-" * 30)

contadorSum = 0 #Donde se almacenará la suma de números

while True: #al ser "infinito" ya que siempre será verdadero hasta que el usuario use el 0, se puede pedir siempre al usuario un número

    numSumar = int(input("Ingrese un número a sumar en secuencias(si ingresa 0 (cero) este terminará): "))
    #si el usuario ingresa cero, este se cierra y pasa al print
    if numSumar == 0:
        break
    #el contador del inicio se actualiza con 0 + los números que vaya agregando el usuario.
    contadorSum = contadorSum + numSumar

print(f"La sumatoria total de los números dados es {contadorSum}")

#Actividad 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos
#fueron necesarios para acertar el número

print("-" * 30)

#Se almacena el número aleatorio
numeroRandom = random.randint(0, 9)

#Se crea la variable para contar la cantidad de intentos
intentos = 0

while True:
    adivinanza = int(input("Te toca adivinar el número entre 0 y 9: "))
    intentos += 1

    if adivinanza == numeroRandom:
        print(f"BINGO ! Le diste al clavo!! Tuviste un total de {intentos} intentos. Nada mal! :D")
        break
    else:
        print("Incorrecto, vuelve a intentarlo!")

#Actividad 6
#Desarrollar un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
print("-" * 30)
print("Ahora por pantalla saldrá todos los números pares comprendidos entre 0 y 100.")
print("-" * 30)

for i in range(100, 0, -2):
    print(i, end=" ")

print("\n")

#Actividad 7
#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

print("-" * 30)

#Pedimos por consola al usuario el número
numeroUsuario = int(input("Ingrese un número entero positivo así se realiza una suma total desde 0 hasta el dado por Usuario: "))

#Por si el usuario decide usar un número negativo
numeroUsuario = abs(numeroUsuario)

#Usamos contador
sumatoriaTotal = 0

for x in range (numeroUsuario + 1):
    sumatoriaTotal += x

print(f"La suma total desde 0 hasta {numeroUsuario} es : {sumatoriaTotal}")

#Actividad 8
#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos
# y cuantos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio.)

print("-" * 30)

#Contadores a usar

pares = 0
impares = 0
positivos = 0
negativos = 0
contadorNumeros = 0


while contadorNumeros < 100: #Acá se ejecutará 100 veces o...
    numeroDado = int(input(f"Ingrese distintos números, para averiguar cuales son pares, impares, negativos y positivos. Vas por el número {contadorNumeros +1}(0 para terminar): ")) #El contadorNumeros +1 es para avisarle al usuario cuantas veces va dando números

    if numeroDado == 0 and contadorNumeros > 0: #Hasta que el usuario presione 0 para salir del programa
        print(f"Programa terminador por el usuario. Se ingresaron {contadorNumeros} números.")
        break

    if numeroDado % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numeroDado > 0:
        positivos += 1
    elif numeroDado < 0:
        negativos += 1

    contadorNumeros += 1

if contadorNumeros > 0:
    print (f"El total de números seleccionados fueron {contadorNumeros}. Ahora la clasificación:")
    print ("########################")
    print (f"Números pares totales: {pares}")
    print (f"Números impares totales: {impares}")
    print (f"Números positivos totales: {positivos}")
    print (f"Números negativos totales: {negativos}")
else:
    print ("No hubo ingreso de números.")

#Actividad 9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: Puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor.)

print("-" * 30)

#Se crea los contadores
sumatoria_Total = 0
contMedia = 0

while contMedia < 100:#Se crea la condición de 100 veces PERO pudiendo salir con el número 0
    numMedia = int(input(f"Ingrese un número para sacar la MEDIA del total, vamos por el número {contMedia + 1}(0 para terminar el programa): "))

    if numMedia == 0 and contMedia > 0:#Aquí se puede salir
        print(f"Programa terminado por el usuario. Se ingresó {contMedia} números")
        break

#Se suma los contadores, ya que sumatoria_Total, va sumando los números que de el usuario por consola.
    sumatoria_Total += numMedia
#Y acá las veces que va ingresando números el usuario, que al final se usará para sacar la media.
    contMedia += 1

if contMedia > 0:
    media = sumatoria_Total / contMedia

    print(f"Se ingresaron un total de {contMedia} números.")
    print(f"La sumatoria total de esos números fue {sumatoria_Total}")
    print(f"Y su media fue de {media}")
else:
    print("No se ingresaron números.")

#Actividad 10
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: Si el usuario ingresa 547, el programa debe mostrar 745.

print("-" * 30)

consolaUsuario = input("Ingrese un número para poder voltearlo: ")#Acá queremos que sea un String

numeroInvertido = "" #Se almacena una cadena vacía

for digitos in consolaUsuario: #Acá recorre cada dígito dado por el usuario.
    numeroInvertido = digitos + numeroInvertido  #Y acá va saliendo el nuevo dígito adelante de

print(f"Ud ingresó {consolaUsuario} y ahora te lo devuelvo en {numeroInvertido}")
