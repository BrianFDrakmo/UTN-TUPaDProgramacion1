import math

#practico 1 : Estructuras Secuenciales
#Actividades
#1 - Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
#2 - Crear un programa que pida al usario su nombre e imprima por pantalla un saludo
#3 - Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia
#4 - Programa usuario el radio de un circulo e imprima por pantalla su area y perímetro
#5 - Programa que pida cantidad de segundos e imprima por pantalla cuantas horas equivale
#6 - Crear un programa al usuario un número e imprima por pantalla la tabala de multiplicar de dicho número
#7 - Crear programa que pida dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
#8 - Crear programa que pida al usuario su altura y peso e imprima por pantalla su índice de masa corporal.
#9 - Crear un programa que pida temperatura
#10 - Porgrama que pida 3 números e imprima por pantalla promedio

#Actividad 1

print ("hola Mundo!")

#Actividad 2

holaNombre = input("Hola, tu nombre?")

print (f"Hola : {holaNombre}")

#Actividad 3

nombreApellido = input("Escriba su nombre y apellido: ")
edad = input("Cuántos años tienes: ")
residencia = input("¿De dónde eres?")

print (f"Bienvenido {nombreApellido}, puede ingresar con esa {edad}, y eres de {residencia}")

#Actividad 4

radioUsuario = float(input("Escribe el radio del circulo para calcular su perímetro: ")) #A tener en cuenta el float o int
PerimetroCirculo = 2 * math.pi * radioUsuario

print (f"El perímetro de su círculo es : {PerimetroCirculo}")

#Actividad 5

segundosUsuario = float(input("Escribe una X cantidad de segundos y te diré cuantas horas son: "))
totalHoras = segundosUsuario / 3600

print (f"En base a los segundos que me diste, el total de horas son {totalHoras}")

#Actividad 6

numeroUsuario = int(input("Coloca un número y te diré la tabla de multiplicar del mismo:: "))

for i in range(1,11):
    resultadoFinal = numeroUsuario * 1
    print(f"{numeroUsuario} x {i} = {resultadoFinal}")

#Actividad 7

numeroEntero1 = int(input("Dame un número entero: "))
numeroEntero2 = int(input("Dame un número entero nuevamente: "))

suma = numeroEntero1 + numeroEntero2
resta = abs(numeroEntero1 - numeroEntero2)
multiplicar = numeroEntero1 * numeroEntero2
dividir = numeroEntero1 / numeroEntero2

print(f"Sumamos ambos números : {numeroEntero1} + {numeroEntero2} = {suma}")
print(f"Restamos ambos números : {numeroEntero1} - {numeroEntero2} = {resta}")
print(f"Multiplicamos ambos números : {numeroEntero1} * {numeroEntero2} = {multiplicar}")
print(f"Dividimos ambos números : {numeroEntero1} / {numeroEntero2} = {dividir}")

#Actividad 8

pesoUsuario = int(input("Cuánto está pesando ud: "))
alturaUsuario = int(input("Cuánto mide ud: "))

alturaUsuarioMetro = alturaUsuario/100 #Se convierte en metros

imc = pesoUsuario / (alturaUsuarioMetro) ** 2
#imcTotal = imc * 10000

print(f"Su IMC es : {imc:.2f}")

#Actividad 9

celsiusUsuario = int(input("Ingrese grados celsius para pasar a Fahrenheit: "))

tempFahrenheit = (celsiusUsuario * 1.8) + 32 #se divide 9/5 y da 1.8

print (f"La temperatura actual en grados Fahrenheit es {tempFahrenheit}")

#Actividad 10

Numero1 = int(input("Dame un número: "))
Numero2 = int(input("Dame otro número: "))
Numero3 = int(input("Y con este el último: "))

promedioTotal = (Numero1 + Numero2 + Numero3) / 3

print(f"El promedio de {Numero1}, {Numero2}, {Numero3} es {promedioTotal}.")