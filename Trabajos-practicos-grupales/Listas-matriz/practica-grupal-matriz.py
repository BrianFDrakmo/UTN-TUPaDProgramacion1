

#Ejercicio 1 : Crear una Matriz de Números

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

matriz = []
numero = 1

for i in range(filas):
    fila_actual = []
    
    for j in range(columnas):
        fila_actual.append(numero)
        numero = numero + 1
    
    matriz.append(fila_actual)

print("Matriz generada:")
for fila in matriz:
    print(fila)

#Ejercicio 2 : Suma de todos los elementos

matrizDos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
totalDos = 0

for i in range(len(matrizDos)):
    suma_fila = 0
    for j in range(len(matrizDos[i])):
        suma_fila = suma_fila + matrizDos[i][j]
    totalDos = totalDos + suma_fila

print(totalDos)

#Ejercicio 3 : Suma de cada fila

for i in range(len(matrizDos)):
    suma_filaTres = 0
    for j in range(len(matrizDos[i])):
        suma_filaTres = suma_filaTres + matrizDos[i][j]
    print("La suma de la fila", i, ":", suma_filaTres)

#Ejercicio 4 : Matriz Transpuesta

matrizCuatro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpuesta = []

for j in range(len(matriz[0])):
    nueva_fila = []
    for i in range(len(matrizCuatro)):
        nueva_fila.append(matrizCuatro[i][j])
    transpuesta.append(nueva_fila)

print(transpuesta)

#Ejercicio 5 : Encontrar el Elemento mayor

matrizQuinta = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
elementoMayor = matrizQuinta[0][0]

for i in range(len(matrizQuinta)):
    for j in range(len(matrizQuinta[i])):
        if matrizQuinta[i][j] > elementoMayor:
            elementoMayor = matrizQuinta[i][j]

print("El número más grande es el ", elementoMayor)

#Ejercicio 6 : Multiplicar una Matriz por un Escalar

matrizSexta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escalar = int(input("Ingresa un número para multiplicarlo"))
resultado = []

for i in range(len(matrizSexta)):
    fila_nueva = []
    for j in range(len(matrizSexta[i])):
        fila_nueva.append(matrizSexta[i][j] * escalar)
    resultado.append(fila_nueva)

print(resultado)

#Ejercicio 7 : Diagonal de una Matriz Cuadrada

matrizSeptima = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal = []

for i in range(len(matrizSeptima)):
    diagonal.append(matrizSeptima[i][i])

print(diagonal)

#Ejercicio 8 : Matriz identidad

n = int(input("Ingrese el tamaño de la matriz."))
identidad = []

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    identidad.append(fila)

for i in range(len(identidad)):
    print(identidad[i])

#Ejercicio 9 : Matriz identidad inversa

nNueve = int(input("Ingrese el tamaño de la matriz inversa "))
identidad_inversa = []

for i in range(n):
    fila_nueve = []
    for j in range(n):
        if j == n - 1 - i:
            fila_nueve.append(1)
        else:
            fila_nueve.append(0)
    identidad_inversa.append(fila_nueve)

for i in range(len(identidad_inversa)):
    print(identidad_inversa[i])

#Ejercicio 10 : Verificar Matriz Simétrica

matrizDecima = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
es_simetrica = True

print("Matriz origen")
for i in range(len(matrizDecima)):
    print(matrizDecima[i])

for i in range(len(matrizDecima)):
    for j in range(len(matrizDecima[i])):
        if matrizDecima[i][j] != matrizDecima[j][i]:
            es_simetrica = False
            break
    if es_simetrica == False:
        break

if es_simetrica == True:
    print("Es simétrica")
else:
    print("NO es simétrica")

#Ejercicio 11 : Rotar una Matriz 90 grados

matrizOnceava = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nOnce = len(matrizOnceava)
matriz_rotada = []

for i in range(nOnce):
    print(matrizOnceava[i])

for i in range(nOnce):
    fila_Once = []
    for j in range(nOnce):
        fila_Once.append(0)
    matriz_rotada.append(fila_Once)

for i in range(nOnce):
    for j in range(nOnce):
        matriz_rotada[j][nOnce - 1 - i] = matrizOnceava[i][j]

print("Matriz rotada")
for i in range(nOnce):
    print(matriz_rotada[i])

#Ejercicio 12 : Analizador y Filtrado de Calificaciones

notas_txt = "45, 88, -5, 92, 30, 110, 75, 60, 15"

notas_lista = notas_txt.split(", ")
print("Lista nueva: ", notas_lista)

aprobado = []
reprobado = []
total_notas = 0
contador_validas = 0

for nota_str in notas_lista:
    nota = int(nota_str)

    if nota < 0 or nota > 100:
        print("Nota inválida; ", nota)
        continue

    total_notas = total_notas + nota
    contador_validas = contador_validas + 1

    if nota >= 60:
        aprobado.append(nota)
    else:
        reprobado.append(nota)

print("Aprobados:", aprobado)
print("Desaprobado:", reprobado)

if contador_validas > 0:
    promedio = total_notas / contador_validas
    print("Promedio total de las notas válidas:", promedio)
else:
    print("No hay notas válidas")

if len(aprobado) >= 2:
    print("Ultimos 2 aprobados: ", aprobado[-2:])
elif len(aprobado) == 1:
    print("Ultimo aprobado:", aprobado[-1:])
else:
    print("No hay suficientes aprobados")

#Ejercicio 13 : Gestor interactivo de Proyectos

tareas = []

while True:
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver resumen")
    print("4. Salir")

    opcion = input("Seleccione una opción con el pad numérico:")

    if opcion == "1":
        tarea = input("Ingrese el nombre de la tarea")

        if tarea in tareas:
            print("Ya está registrada")
        else:
            tareas.append(tarea)
            print("Se agregó correctamente")

    elif opcion == "2":
        tarea = input("Ingrese el nombre de la tarea para eliminar")

        if tarea in tareas:
            tareas.remove(tarea)
            print("Se eliminó correctamente")
        else:
            print("ERROR 404! Not Found")

    elif opcion == "3":
        print("Ver resumen")
        print("Todas las tareas ", len(tareas))

        if len(tareas) > 0:
            print("primeras 3 tareas ", tareas[:3])
        else:
            print("No hay tareas registradas")

    elif opcion == "4":
        print("ADIOS!")
        break

    else:
        print("Opción que no corresponde a un abonado a nuestro servicio, use el pad numérico del 1 al 4. Gracias! :D")