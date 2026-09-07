#Práctico 2: Funciones en Python

#Actividades
#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: "Hola mundo!". Llamar a esta función desde el programa principal

def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: "Hola Marcos!". Llamar a esta función desde el programa principal solicitando
#el nombre al usuario

def saludar_usuario(nombre):
    return f"Hola {nombre}"


nombre_usuario = input("Ingresá tu nombre ")

mensaje = saludar_usuario(nombre_usuario)
print(mensaje)

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: "Soy [nombre] [apellido
# , tengo [edad] años y vivo en [residencia]." Pedir los datos al usuario y llamar a esta función con los valores ingresador

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

datos_nombre = input("Ingresá tu nombre ")
datos_apellido = input("Ingresá tu apellido ")
datos_edad = input("Tu edad ")
datos_residencia = input("Donde resides? ")

mensaje_final = informacion_personal(datos_nombre, datos_apellido, datos_edad, datos_residencia)
print(mensaje_final)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio)
#que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
pi = 3.1416

def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio_usuario = float(input("Ingresá el radio del círculo para calcular: "))

area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"El área de tu círculo es {area:.2f} y su perímetro fue de {perimetro:.2f}.")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas
#correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos_usuario = float(input("Ingresa la cantidad de segundos para saber cuanto equivale a horas: "))
horas = segundos_a_horas(segundos_usuario)

print(f"{segundos_usuario} segundos equivale a {horas:.2f} horas.")

#6. Crear una función llamada operaciones_basicas(a,b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos
# multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

numero1 = float(input("Ingresá tu primer número: "))
numero2 = float(input("Ingresá tu segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(numero1, numero2)

print(f"La sumatoria entre {numero1} y {numero2} = {suma}")
print(f"La resta entre {numero1} y {numero2} = {resta}")
print(f"La multiplicación entre {numero1} y {numero2} = {multiplicacion}")
print(f"La división entre {numero1} y {numero2} = {division}")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal
#(IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resutlado con dos decimales.

def calcular_imc(peso, altura):
    return peso/ (altura ** 2)

peso_usuario = float(input("Ingresá tu peso en KG: "))
altura_usuario = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso_usuario, altura_usuario)

print(f"Tu IMC es de {imc:.2f}")

#9. Crear una función llamada celcius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente
#en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función

def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

celsius_usuario = float(input("Ingresa la temperatura actual en °C : "))
fahrenheit = celsius_a_fahrenheit(celsius_usuario)

print(f"{celsius_usuario}°C equivale a {fahrenheit:.2f}°F.")

#10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelkva el promedio de ellos
#Solicitar los números al usuario usando esta función

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

nota1 = float(input("Ingresá tu primera nota para sacar tu promedio: "))
nota2 = float(input("Ingresá tu segunda nota: "))
nota3 = float(input("E ingresá la última nota: "))

promedio = calcular_promedio(nota1, nota2, nota3)

print(f"Tu promedio de {nota1}, {nota2} y {nota3} = {promedio:.2f}.")