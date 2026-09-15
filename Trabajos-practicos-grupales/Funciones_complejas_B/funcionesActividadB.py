# Diccionario Alumnos

alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

#Lista Materia 2 dimensiones

materias = [
    ["Ciencias", 0, 0, 0],
    ["Historia", 0, 0, 0],
    ["Geografia", 0, 0, 0],
    ["Matematicas", 0, 0, 0],
    ["Fisica", 0, 0, 0]
]

#Lista Notas Finales

notasFinales = [
    ["Rodolfo Fernandez", 0],
    ["Luis Gomez", 0],
    ["Andrea Pereira", 0],
    ["Juan Cruz Gonzales", 0]
]

# =======================
# Validaciones Actividad B
# =======================

def validar_nota(mensaje):
    nota = input(mensaje)
    while not nota.isdigit() or int(nota) < 0 or int(nota) > 10:
        print("Error: la nota debe ser un número entre 0 y 10.")
        nota = input(mensaje)
    return int(nota)

def cargar_notas_alumno(nombre):
    for materia in materias:
        print(f"\nIngrese las notas para la materia {materia[0]}")
        nota1 = validar_nota("Nota 1: ")
        nota2 = validar_nota("Nota 2: ")

        nota_final = (nota1 + nota2) / 2

        materia[1] = nota1
        materia[2] = nota2
        materia[3] = nota_final

        print(f"Nota Final: {nota_final}")

def mostrar_materias():
    print("\n===== LISTA DE MATERIAS =====")
    print(f"{'Materia':<15}{'Nota 1':<10}{'Nota 2':<10}{'Nota Final':<10}")
    print("-" * 45)
    for materia in materias:
        print(f"{materia[0]:<15}{materia[1]:<10}{materia[2]:<10}{materia[3]:<10}")

def materia_mas_alta(nombre_alumno):
    mejor = materias[0]
    for materia in materias:
        if materia[3] > mejor[3]:
            mejor = materia
    print(f"\nLa materia con la calificación más alta de {nombre_alumno} " f"es {mejor[0]} con {mejor[3]}")

def calcular_promedio_general():
    contador = 0
    for legajo, nombre in alumnos.items():
        suma = 0
        for materia in materias:
            suma += materia[3]
        promedio = suma / len(materias)
        
        notasFinales[contador][0] = nombre
        notasFinales[contador][1] = promedio
        
        contador += 1
    return notasFinales

def mostrar_mejor_promedio():
    mejor = notasFinales[0]
    for alumno in notasFinales:
        if alumno[1] > mejor[1]:
            mejor = alumno
    print(f"\n===== MEJOR PROMEDIO =====")
    print(f"El alumno con el mejor promedio es {mejor[0]} con {mejor[1]:.2f}")