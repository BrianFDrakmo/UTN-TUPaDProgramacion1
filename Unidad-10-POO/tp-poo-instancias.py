#Actividad 1

class Celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def buscar_celda(self, fila: int, columna: int):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda
        return None

    def obtener_valor(self, fila: int, columna: int):
        celda = self.buscar_celda(fila, columna)
        if celda is not None:
            return celda.valor
        else:
            return ("La fila y columna indicada no ha sido asignada en ninguna celda.")

#Actividad 2

class Alumno:
    def __init__(self, nombreCompleto, edad, legajo)