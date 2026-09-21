import os

ARCHIVO = "productos.txt"

# ---------- 2 y 4: Leer y cargar en lista de diccionarios ----------
def cargar_productos():
    productos = []

    if not os.path.exists(ARCHIVO):
        print("¡¡¡El archivo no existe, se creará con productos iniciales!!!")
        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            archivo.write("Lapicera,120.5,30\n")
            archivo.write("Cuaderno,350.0,15\n")
            archivo.write("Goma,50.0,40\n")

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            nombre, precio, cantidad = linea.split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos

# ---------- 2: Mostrar productos ----------
def mostrar_productos(productos):
    print("\n--- Lista de productos ---")
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

# ---------- 3: Agregar producto desde teclado ----------
def agregar_producto(productos):
    nombre = input("Nombre del nuevo producto: ").strip()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto agregado!!!")

# ---------- 5: Buscar producto por nombre ----------
def buscar_producto(productos):
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()
    for producto in productos:
        if producto["nombre"].lower() == nombre:
            print(f"Encontrado → Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            return
    print("Producto no encontrado!!!")

# ---------- 6: Guardar cambios ----------
def guardar_productos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Archivo actualizado correctamente.")

# ---------- Programa principal ----------
def main():
    productos = cargar_productos()
    mostrar_productos(productos)

    agregar_producto(productos)
    mostrar_productos(productos)

    buscar_producto(productos)

    guardar_productos(productos)

if __name__ == "__main__":
    main()