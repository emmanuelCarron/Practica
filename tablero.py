from copy import deepcopy

class Tablero:
    '''Tablero es un tablero vacío de celdas cuadradas de un ancho y alto determinado de celdas.
    Las celdas vacías están representadas por 0
    Operaciones:
        + Reset (limpia el tablero)
        + Mostrar (imprime el tablero en pantalla)
        + Colorear celdas
        + Colocar pieza (en una celda en específico)
    Condiciones:
        + Alto y ancho mayor a 0
        + No puede haber dos piezas en la misma celda
    '''

    def reset(self):
        '''Limpia el tablero'''
        self.__estado = [['0' for columna in range(self.ancho)] for fila in range(self.alto)]
        self.__modificaciones = deepcopy(self.__estado)

    def __init__(self, ancho, alto):
        '''Constructor de mi TAD, toma ancho y alto del tablero'''
        self.ancho = ancho
        self.alto = alto
        self.reset()

    def mostrar(self):
        for fila in self.__estado:
            for columna in fila:
                print(columna, end='')
            print('')

    def colocar_pieza(self, columna, fila, pieza):
        self.__modificaciones[fila][columna] = pieza 

    def guardar_estado(self):
        self.__estado = deepcopy(self.__modificaciones)
