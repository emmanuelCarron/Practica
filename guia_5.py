class AlumnoMateria:

    def __init__(self, nombre, nota, materia):
        #función que inicializa una variable AlumnoMateria
        self.nombre = nombre
        self.nota = nota
        self.materia = materia
        self.__condicion = ""

    def __str__(self):
        return (f"{self.nombre}, {self.nota}, {self.materia}")

    def mostrar_estado(self)->str:
        '''calcula si esta regular, promocionado, o libre.'''
        if self.nota < 4:
            self.__condicion = "Libre"
        elif self.nota >= 7:
            self.__condicion = "Promocional"
        else:
            self.__condicion = "Regular"
        return self.__condicion


class RegistroAlumnoMateria:

    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia
        self.__notas = () 
        self.__condicion = "Regular"

    def __str__(self):
        return (f"{self.nombre}, {self.__notas}, {self.materia}, {self.__condicion}")

    def calcular_promedio(self):
        return sum(self.__notas) / len(self.__notas)

    def condicion(self)->str:
        '''calcula si esta regular, promocionado, o libre.'''
        promedio = self.calcular_promedio()
        if promedio < 4:
            self.__condicion = "Libre"
        #elif promedio >= 7 and len([i for i in self.__notas if i<6]) == 0:
        elif promedio >= 7 and min(self.__notas) < 6:
            self.__condicion = "Promocional"
        else:
            self.__condicion = "Regular"
        return self.__condicion
    
    def agregar_nota(self, nota): #puede ser int o una tupla de ints
        if isinstance(nota, (tuple)):
            self.__notas = self.__notas + nota
        elif isinstance(nota, (int)):
            n = [nota]
            self.__notas = self.__notas + tuple(n)

    def mostrar_notas(self):
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
        return (self.par == otro.par)

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return "{}".format(self.par)

    def es_origen(self):
        """Me dice si el punto corresponde al origen del plano"""
        return (self.par == (0,0))

    def mover(self,dx,dy):
        """Mueve el punto dx lugares en x y dx lugares en y"""
        self.par = (self.par[0] + dx,self.par[1] + dy)
                                               
    def distancia(self,otro):
        return (((self.par[0]-otro.par[0])**2) + ((self.par[1]-otro.par[1])**2))**(1/2)

    def distancia_origen(self):
        return self.distancia(Punto(0,0))


def mas_lejos(puntos:[Punto]) -> Punto:
    #guardamos las distancias al origen en una lista
    distancias = [punto.distancia_origen() for punto in puntos]
    #el índice de la mayor distancia es el índice del punto lejano al origen
    indice_lejano = distancias.index(max(distancias))
    return puntos[indice_lejano]

'''         3           '''


alumno1 = AlumnoMateria("Juan", 5, "Lengua")
print(alumno1.mostrar_estado())
print(alumno1)

alumno2 = RegistroAlumnoMateria("Diego", "Matemática")
print(alumno2)
alumno2.agregar_nota(9)
print(alumno2.mostrar_notas())
print(alumno2.calcular_promedio())
alumno2.agregar_nota((4,6,7))
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