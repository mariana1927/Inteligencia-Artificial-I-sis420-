#%%
import math
from busqueda_Laberinto import LaberinroBusqueda, aestrella

#%%
Mapa_Laberinto = """
            IIIIIIIIIIIIIIIIIIIIIIIIIIIIII
            I         I              I   I
            I IIII    IIIIIIII        X  I
            I    I                   I   I
            I    III     IIII   IIIIII   I
            I         IIII      I        I
            I               I   I   IIII I
            I     IIIIII    I       I    I
            I O      I      I            I
            IIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        """
#convierte en una lista y divide en base a los limites
Mapa_Laberinto = [list(x) for x in Mapa_Laberinto.split("\n") if x]

#diccionario para determinar los costos de una ruta que un '.' pude tomar
COSTOS = {
    "arriba": 1.0,
    "abajo": 1.0,
    "izquierda": 1.0,
    "derecha": 1.0,
    "arriba izquierda": 2.1,
    "arriba derecha": 2.1,
    "abajo izquierda": 2.1,
    "abajo derecha": 2.1,
}

#%%
#clase base donde se tiene que crear un nuevo problema donde se defince que hay que indicar 
class JuegoLaberinto(LaberinroBusqueda):

    #definicion de funcion para crear el objeto donde se realizará la busqueda, se llama automaticamente
    def __init__(self, tablero):
        self.tablero = tablero
        self.estado_objetivo = (0, 0)
        #range(len()) es representa la secuencia de la lista o cadena del tablero
        for y in range(len(self.tablero)):
            for x in range(len(self.tablero[y])):
                if self.tablero[y][x].lower() == "o":
                    self.estado_inicial = (x, y)
                elif self.tablero[y][x].lower() == "x":
                    self.estado_objetivo = (x, y)

        super(JuegoLaberinto, self).__init__(estado_inicial=self.estado_inicial)

    #definicion de funcion que devueve las acciones que estan disponibles y que son especificas del Laberinto
    def acciones(self, estado):
        acciones = []
        for accion in list(COSTOS.keys()):
            nuevox, nuevoy = self.resultado(estado, accion)
            if self.tablero[nuevoy][nuevox] != "I":
                #append agrega nuevas acciones a la lista
                acciones.append(accion)
        return acciones

    #definicion de funcion que devuelve el nuevo estado seguidamente de atribuir una accion a ese estado
    def resultado(self, estado, accion):
        x, y = estado

        if accion.count("arriba"):
            y -= 1
        if accion.count("abajo"):
            y += 1
        if accion.count("izquierda"):
            x -= 1
        if accion.count("derecha"):
            x += 1

        estado_nuevo = (x, y)
        return estado_nuevo

    ##definicion de funcion que devuelve un valor verdadeo (true) si es el estado al que se quiere llegar
    #y devuelve un valor falso (false) si no es el estado al que se quiere llegar
    def es_objetivo(self, estado):
        return estado == self.estado_objetivo

    #definicion de funcion que devuelve el costo de realizar una accion el siguiente estado a partir del estado inicial
    def costo(self, estado, accion, estado2):
        return COSTOS[accion]

    #definicion de funcion heuristica donde devuelve el costo aproximado para llegar llegar al objetivo de solucion
    def heuristica(self, estado):
        x, y = estado
        gx, gy = self.estado_objetivo
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)

#%%
#definicion de funcion principal del Laberinto
def main():
    problema = JuegoLaberinto(Mapa_Laberinto)
    resultado = aestrella(problema, busqueda_en_grafo=True)
    camino = [x[1] for x in resultado.camino()]

    #range(len()) es representa la secuencia de la lista o cadena del Mapa del Laberinto
    for y in range(len(Mapa_Laberinto)):
        for x in range(len(Mapa_Laberinto[y])):
            if (x, y) == problema.estado_inicial:
                print("o", end='')
            elif (x, y) == problema.estado_objetivo:
                print("x", end='')
            elif (x, y) in camino:
                print(".", end='')
            else:
                print(Mapa_Laberinto[y][x], end='')
        print()

#%%
#se implementa para proteger parte del código
#así se puede estar seguro de que este bloque solo se ejecutará si nuestro módulo es el programa principal (main)
if __name__ == "__main__":
    main()