import random
from statistics import mode, median, mean


#Actividad TP2
#1- Escribir programa que solicite edad del usuario. Si es mayor a 18 deberá mostrar un mensaje en patalla que diga "Es mayor de edad" 
#2- Escribir programa que solicite su nota al usuario. Si es mayor o igual a 6, es APROBADO, sino DESAPROBADO.
#3- Escribir programa que ingrese solo números pares. Si el usuario ingresa un número par, imprime "Haz ingresado un número par", sino imprime
#"Por favor, ingrese un número par". Nota: Investigar el uso del operador módulo (%) en Python para evaluar si un número es par o impar.
#4- Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#    niño: menor a 12
#    adolescente: mayor o igual a 12 y menor a 18
#    adulto joven: mayor o igual a 18 y menor a 30
#    adulto: mayor o igual que 30.
#5- Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña
#de longitud adecuada, imprimir por pantalla "Ha ingresado una constraseña correcta; en caso contrario, imprimir "Por favor, ingrese una pass de entre
#8 y 14 caracteres. Nota: Investigar el uso de la función len() en Python
#6- El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la medida y la media de dichos
#números. Escribir programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compara para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#7- Escribir programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e 
#imprimir el string resultante por pantalla; en caso contrario dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
#8- Escribir programa que solicite al usuario que ingrese su nombre y el número 1,2 o 3 dependiendo de la opción:
#    1- Quiere su nombre en mayusculas
#    2- Quiere su nombre en minusculas
#    3- Quiere su nombre con la primera letra mayuscula
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
#upper(), lower(), title()
#9- Escribe programa que pida al usuario la magnitud del terremoto, clasifique la magnitudes.
#10- Utilizando la tabla, ejecute un programa que pregunte al usuario hemisferio, mes y día. Y dependiendo de eso saldrá si se encuentra en otoño, invierno, primavera o verano.

#Actividad 1


edad = input("Cuál es su edad?")

if int(edad) >= 18:
    print ("Es mayor de edad.")
else:
    print ("Es menor de edad.")

#Actividad 2

nota = int(input("Cuál fue tu nota para saber si aprobaste o no."))

if nota >=6 and nota <= 10:
    print ("APROBADO REY.")
else:
    print ("Desaprobado. No te preocupes, puedes mejorar.")

#Actividad 3

numero = int(input("Ingresa un número y te diré si es par o no."))

if numero % 2 == 0:
    print (f"El número {numero} es par.")
else:
    print (f"El número {numero} es impar.")

#Actividad 4

edadUsuario = int(input("Cuál es tu edad?"))

if edadUsuario < 12:
    print("Sos un niño.")
elif edadUsuario >= 12 and edadUsuario < 18:
    print("Sos un adolescente.")
elif edadUsuario >= 18 and edadUsuario < 30:
    print("Sos un joven adulto.")
elif edadUsuario >= 30:
    print("Sos un adulto.")

#Actividad 5

password = input("Ingresa una contraseña entre 8 y 14 caracteres.")

if len(password) >= 8 and len(password) <= 14:
    print("Contraseña correcta.")
else:
    print("Recuerda que debe tener entre 8 y 14 caracteres.")

#Actividad 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Se crea las variables para calcular
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Ver los resultados
print (f"Lista de números: {numeros_aleatorios}")
print (f"Media: {media}")
print (f"Mediana: {mediana}")
print (f"Moda: {moda}")

#Comparar el sesgo

if media> mediana > moda:
    print ("Es Sesgo positivo o a la derecha.")
elif media < mediana < moda:
    print ("Es Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print ("Sin sesgo")
else:
    print ("No se puede determinar sesgo.")

#Actividad 7

palabraUsuario = input("Ingrese palabra o frase.")

if palabraUsuario[-1] in "aeiouAEIOU":
    print (palabraUsuario + "!")
else:
    print (palabraUsuario)

#Actividad 8

nombreUsuario = input("Ingrese su nombre.")

print("Elige entre 1,2 o 3 siendo estas: ")
print("Opción 1: Tu nombre todo en mayúsculas.")
print("Opción 2: Tu nombre todo en minúsculas.")
print("Opción 3: Tu nombre con la primera inicial en mayúscula.")

opciones = input("Ingrese la opción que desea (1 ,2 o 3): ")

match opciones:
    case "1":
        print (nombreUsuario.upper())
    case "2":
        print (nombreUsuario.lower())
    case "3":
        print (nombreUsuario.title())
    case _:
        print ("Opción incorrecta, debe elegir 1, 2 o 3.")

#Actividad 9

terremoto = int(input("De cuánto fue el sismo sentido por el usuario? Puede ser de 3 a 7"))


if terremoto < 3:
    print("Muy leve.")
elif terremoto >= 3 and terremoto < 4:
    print("Leve.")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado.")
elif terremoto >=5 and terremoto < 6:
    print("Fuerte.")
elif terremoto >=6 and terremoto < 7:
    print("Muy fuerte.")
else:
    print("EXTREMO! TERREMOTO!!")

#Actividad 10

hemisferioUsuario = input("En cuál hemisferio te encuentras? Norte o Sur.").lower()
periodoMes = input("En que mes te encuentras?").lower()
periodoDia = int(input("Y en que día te encuentras? En número."))

#Determina hemisferio Sur

if hemisferioUsuario == "sur":
    
    if (periodoMes == "diciembre" and periodoDia >= 21) or (periodoMes in ["enero", "febrero"]) or (periodoMes == "marzo" and periodoDia <= 20):
        print("Es verano en el hemisferio sur.")
    elif (periodoMes == "marzo" and periodoDia >= 21) or (periodoMes in ["abril", "mayo"]) or (periodoMes == "junio" and periodoDia <= 20):
        print("Es otoño en el hemisferio sur.")
    elif (periodoMes == "junio" and periodoDia >= 21) or (periodoMes in ["julio", "agosto"]) or (periodoMes == "septiembre" and periodoDia <= 20):
        print("Es invierno en el hemisferio sur.")
    else:
        print("Es primavera en el hemisferio sur.")

#Determina hemisferio Norte

if hemisferioUsuario == "norte":

    if (periodoMes == "diciembre" and periodoDia >= 21) or (periodoMes in ["enero", "febrero"]) or (periodoMes == "marzo" and periodoDia <= 20):
        print("Es invierno en el hemisferio sur.")
    elif (periodoMes == "marzo" and periodoDia >= 21) or (periodoMes in ["abril", "mayo"]) or (periodoMes == "junio" and periodoDia <= 20):
        print("Es primavera en el hemisferio sur.")
    elif (periodoMes == "junio" and periodoDia >= 21) or (periodoMes in ["julio", "agosto"]) or (periodoMes == "septiembre" and periodoDia <= 20):
        print("Es verano en el hemisferio sur.")
    else:
        print("Es otoño en el hemisferio sur.")