from math import pi

class AlumnoMateria:
    '''
    AlumnoMateria agrupa el nombre de un alumno, una nota y la materia
    en la que obtuvo dicha calificación.

    Operaciones:
        + Mostrar estado (muestra la condición de cursado del alumno)
    Condiciones:
        + Su representación str contiene los atributos ingresados en el constructor
        + Condición Libre: nota menor a 4
        + Condición Promocional: nota 7 o más
        + Condición Regular: nota entre 4 y 6 
    '''
    def __init__(self, nombre, nota, materia):
        ''' Constructor de TAD, toma nombre del alumno, nota y materia'''
        self.nombre = nombre
        self.nota = nota
        self.materia = materia
        self.__condicion = ""

    def __str__(self):
        return f"{self.nombre}, {self.nota}, {self.materia}"

    def mostrar_estado(self)->str:
        ''' Calcula si esta regular, promocionado, o libre.'''
        if self.nota < 4:
            self.__condicion = "Libre"
        elif self.nota >= 7:
            self.__condicion = "Promocional"
        else:
            self.__condicion = "Regular"
        return self.__condicion


class RegistroAlumnoMateria:
    '''
    RegistroAlumnoMateria agrupa nombre de alumno, materia y permite varias notas

    Operaciones:
        + Calcular promedio
        + Condición (regular, promocional o libre según el promedio)
        + Agregar nota
        + Mostrar nota

    Condiciones:
        + La condición se calcula en base al promedio
    '''
    def __init__(self, nombre, materia):
        ''' Constructor de TAD, toma nombre de alumno y materia '''
        self.nombre = nombre
        self.materia = materia
        self.__notas = [] 
        self.__condicion = "Regular"

    def __str__(self):
        return f"{self.nombre}, {self.__notas}, {self.materia}, {self.__condicion}"

    def calcular_promedio(self):
        ''' Devuelve promedio de las notas '''
        return sum(self.__notas) / len(self.__notas)

    def condicion(self)->str:
        ''' Devuelve una cadena con la condición de cursado del alumno'''
        promedio = self.calcular_promedio()
        if promedio < 4:
            self.__condicion = "Libre"
        elif promedio >= 7 and min(self.__notas) >= 6:
            self.__condicion = "Promocional"
        else:
            self.__condicion = "Regular"
        return self.__condicion
    
    def agregar_nota(self, nota):
        ''' Agrega nota a la lista de notas '''
        self.__notas = self.__notas.append(nota)

    def mostrar_notas(self):
        ''' Devuelve la lista de notas '''
        return self.__notas

'''         2           '''

class Punto:
    """Un punto en el espacio bi dimensional:
    - coordenada x
    - coordenada y
    """

    def __init__(self, x=0, y=0): # si no paso x e y se considera que el punto es (0,0) 
        self.par = (x,y)

    def __eq__(self, otro):
        """Devolver True si self es igual a otro."""
        return self.par == otro.par

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return f"{self.par}"

    def es_origen(self):
        """Me dice si el punto corresponde al origen del plano"""
        return self.par == (0,0)

    def mover(self,dx,dy):
        """Mueve el punto dx lugares en x y dx lugares en y"""
        self.par = (self.par[0] + dx,self.par[1] + dy)
                                               
    def distancia(self,otro):
        return (((self.par[0]-otro.par[0])**2) + ((self.par[1]-otro.par[1])**2))**(1/2)

    def distancia_origen(self):
        return self.distancia(Punto(0,0))


def mas_lejos(puntos:[Punto]) -> Punto:
    ''' Guardamos las distancias al origen en una lista '''
    distancias = [punto.distancia_origen() for punto in puntos]
    ''' El índice de la mayor distancia es el índice del punto lejano al origen '''
    indice_lejano = distancias.index(max(distancias))
    return puntos[indice_lejano]

'''         3           '''

class Circulo:
    ''' 
    Circulo define un círculo apartir de su centro y radio

    Operaciones:
        + Diámetro
        + Perímetro
        + Área
        + Método especial eq
        + Mover

    Condiciones:
        + El centro debe ser un par ordenado
        + Dos circunferencias son iguales si radio y centro son iguales
        + El radio debe ser mayor a 0
    '''

    def __init__(self, centro, radio):
        ''' Constructor de TAD, toma un par ordenado representando el centro y un radio '''
        self.centro = centro
        if radio <= 0:
            raise ValueError("El radio de una circunferencia debe ser positivo")
        else:
            self.radio = radio
    
    def diametro(self):
        ''' Devuelve el diámetro de la circunferencia '''
        return (2*self.radio)

    def perimetro(self):
        ''' Devuelve el perímetro de la circunferencia'''
        return (2*pi*self.radio)

    def area(self):
        ''' Devuelve el área del círculo '''
        return (pi*(self.radio**2))

    def __eq__(self, otro):
        ''' Compara el círculo con otro dado y devuelve True si son equivalentes '''
        return (self.centro == otro.centro and self.radio == otro.radio)

    def mover(self, nuevo_centro):
        ''' Mueve el círculo cambiando de coordenadas el centro '''
        self.centro = nuevo_centro

'''         4           '''

class Fraccion:
    '''
    Fraccion es un número racional escrito con numerador y denominador

    Operaciones:
        + Suma

    Condiciones:
        + Denominador distinto de 0
        + Debemos poder comparar fracciones equivalentes
    '''
    def __init__(self, num, den): 
        ''' Constructor, recibe numerador y denominador '''
        self.numerador = num
        if den == 0:
            raise ZeroDivisionError("Recuerda que el denominador no puede ser 0")
        else:
            self.denominador = den

    def __str__(self):
        ''' Devuelve numerado/denominador '''
        return (f"{self.numerador}/{self.denominador}")
    
    def __eq__(self, otro):
        ''' Dos fracciones serán equivalentes si resolvemos los cocientes y éstos son iguales
        En ese caso devuelve True
        '''
        return ((self.numerador/self.denominador)==(otro.numerador/otro.denominador))

    def comun_divisor(self, a, b):
        ''' Devuelve el común divisor entre a y b '''
        return a if not b else self.comun_divisor(b, a%b)

    def min_com_mult(self, a, b):
        ''' Devuelve el mínimo común múltiplo entre a y b '''
        return a*b//self.comun_divisor(a, b)

    def sumar_fracciones(self, otro):
        ''' Adición con otra fracción dada calculando denominador y numerador.
        Devuelve otra instancia de Fracción con el numerador y denominador obtenidos.
        '''
        denominador = self.min_com_mult(self.denominador, otro.denominador)
        numerador = (denominador//self.denominador*self.numerador)+(denominador//otro.denominador*otro.numerador)
        return Fraccion(numerador,denominador)


'''         5           '''

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




#------------------------------------------------------------
alumno1 = AlumnoMateria("Juan", 5, "Lengua")
print(alumno1.mostrar_estado())
print(alumno1)

alumno2 = RegistroAlumnoMateria("Diego", "Matemática")
print(alumno2)
alumno2.agregar_nota(9)
print(alumno2.mostrar_notas())
print(alumno2.calcular_promedio())
alumno2.agregar_nota(4)
print(alumno2.mostrar_notas())
print(alumno2.calcular_promedio())
print(alumno2.condicion())

A = Punto(2,3)
B = Punto(5,5)
C = Punto(1,5)

print(A.distancia(B))
print(A.distancia_origen())
print(B.distancia_origen())
print(C.distancia_origen())

print(mas_lejos([Punto(2,3), Punto(5,5), Punto(1,5)]))

c= Circulo((0,0), 4.5)
print(c.diametro())
print(c.area())
print(c.perimetro())

un_medio = Fraccion(1,2)
print(un_medio)
uno = Fraccion(2,2)
print(uno)
dos_tercios = Fraccion(2,3)
print(un_medio.sumar_fracciones(dos_tercios))
