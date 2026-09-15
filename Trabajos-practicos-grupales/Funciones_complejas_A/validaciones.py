"""Una empresa de software les brinda a sus empleados como parte de sus beneficios
la posibilidad de acceder de forma gratuita a una máquina de Golosinas. Nuestra tarea será la programación de las funcionalidades necesarias
para llevar adelante este beneficio.

Codifique la siguiente Lista de 2 dimensiones "golosinas", que se corresponde a una maquina expendedora de golosinas
donde la columna 0 es el codigo de la golosina, la columna 1 es la golosina, y la columna 2 es la cantidad (stock actual de golosinas.)"""

#golosinas = [Columna 0 (Codigo golosina) | Columna 1 (Nombre golosina) | Columna 2 (Cantidad golosina)]
golosinas = [[1, "KitKat",20],
             [2, "Chicles",50],
             [3, "Caramelos de Menta",50],
             [4, "Huevo Kinder",10],
             [5, "Chetoos",10],
             [6, "Twix",10],
             [7, "M&M'S",10],
             [8, "Ppas Lays",2],
             [9, "Milkybar",10],
             [10, "Alfajor Tofi",15],
             [11, "Lata Coca-Cola",20],
             [12, "Chitos",10]]

"""Codifique un Diccionario "empleados" donde el par clave valor, representa al legajo de un empleado y a su nombre"""

empleados = {
        1100: "José Alonse",
        1200: "Federico Pacheco",
        1300: "Nelson Pereira",
        1400: "Osvaldo Tejada",
        1500: "Gastón García"
}

clavesTecnico = ("admin", "CCCDDD", 2020)

golosinasPedidas = []

#Validaciones A

#####################
def pedirGolosina():
    confirmarLegajo = int(input("Ingrese el número de su legajo de empleado, por favor! "))
    if confirmarLegajo in empleados:
        print(f"Bienvenido, {empleados[confirmarLegajo]}")
        while True:
            codigoGolosina = int(input("Ingrese el código de su golosina, si deseas salir use el código 99. "))
            if codigoGolosina == 99:
                break
            encontrada = False
            for golosina in golosinas:
                if golosina[0] == codigoGolosina:
                    encontrada = True
                    if golosina[2] > 0:
                        golosina[2] -= 1
                        registrarPedido(golosina)
                    else:
                        print(f"Lo sentimos, la golosina {golosina[1]} no se encuentra disponible.")
                    break
            if not encontrada:
                print("Codigo inválido")
    else:
        print("Usted no es un empleado de la empresa.")
        return

#####################
def registrarPedido(golosina):
    for fila in golosinasPedidas:
        if fila[0] == golosina[0]:
            fila[2] += 1
            return
    golosinasPedidas.append([golosinas[0], golosina[1], 1])

#####################
def mostrarGolosinas():
    print("##### Golosinas Disponibles #####")
    for golosina in golosinas:
        print(f"Codigo: {golosina[0]} , {golosina[1]} , Stock: {golosina[2]}")

######################
def rellenarGolosinas():
    print("##### Autenticación #####")

    for claveAdmin in clavesTecnico:
        ingreso = input("Ingrese una clave Técnica: ")
        if ingreso != str(claveAdmin):
            print("No tienes autorización")
            return

    print("Acceso autorizado.")

    codigo = int(input("Código de golosina a recargar: "))

    for golosina in golosinas: 
        if golosina[0] == codigo:
            cantidad = int(input("Cantidad a recargar: "))
            if cantidad > 0:
                golosina[2] += cantidad
                print(f"Stock actualizado")
            else:
                print("La cantidad debe ser mayor a 0")

    print("Código de golosina inválido")

####################
def apagarMaquina():
    print("##### Pedidos realizados #####")
    total = 0
    for fila in golosinasPedidas:
        print(f"Código: {fila[0]} , {fila[1]} , Cantidad {fila[2]}")
        total += fila[2]
    print(f"Total de golosinas pedidas {total}")
