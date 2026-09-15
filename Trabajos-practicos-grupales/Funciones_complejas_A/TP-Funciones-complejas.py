from validaciones import *

#Practica A
#Mostrar golosinas

while True:
    print("a.Pedir golosina")
    print("b.Mostrar golosinas")
    print("c.Rellenar golosinas")
    print("d.Apagar máquina")
    opcion = input("Elije una opción: ").lower()

    if opcion == "a":
        pedirGolosina()
    elif opcion == "b":
        mostrarGolosinas()
    elif opcion == "c":
        rellenarGolosinas()
    elif opcion == "d":
        apagarMaquina()
        break
    else:
        print("Opción inválida")


#Pedir Golosinas

while True:

    codigoGolosina = int(input("Ingrese el código de su golosina, si deseas salir use el código 99. "))

    #Salida del bucle
    if codigoGolosina == 99:
        break
    
    #Disminuir golosina
    encontrada = False
    for golosina in golosinas:
        if golosina[0] == codigoGolosina:
            encontrada = True
            if golosina[2] > 0:
                golosina[2] -= 1
                registrarPedido(golosina)
            else:
                print(f"Lo sentimos, la golosina {golosina} no se encuentra disponible, seleccione otra golosina o ingresa 99 si deseas salir. ")
            break
        if not encontrada:
            print("Codigo inválido")