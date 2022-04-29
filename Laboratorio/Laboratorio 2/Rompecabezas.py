#%%
from Piezas import Pieza
#%%
def rompecabezas_solucion(estado_inicial, solucion):
    resuelto = False
    piezas_utilizadas = []
    piezas_frontera = []

    pieza_raiz = Pieza(estado_inicial)
    piezas_frontera.append(pieza_raiz)#extiende la lista
    while (not resuelto) and len(piezas_frontera) != 0:
        pieza_actual = piezas_frontera.pop(0)
        #extrae la pieza y la añade a las ya utilizadas
        piezas_utilizadas.append(pieza_actual)
        if pieza_actual.get_estado() == solucion:
            #solucion del rompecabezas encontrada
            resuelto = True
            return pieza_actual
        else:
            #piezas
            estado_pieza = pieza_actual.get_estado()

            #en lado izquierdo
            pieza = [estado_pieza[1], estado_pieza[0], estado_pieza[2], estado_pieza[4], estado_pieza[3],
                    estado_pieza[6], estado_pieza[5], estado_pieza[8], estado_pieza[7], estado_pieza[9]]
            pieza_izquierda = Pieza(pieza)
            if not pieza_izquierda.en_lista(piezas_utilizadas) and not pieza_izquierda.en_lista(piezas_frontera):
                piezas_frontera.append(pieza_izquierda)

            #en el centro
            pieza = [estado_pieza[0], estado_pieza[2], estado_pieza[1], estado_pieza[3], estado_pieza[4],
                    estado_pieza[5], estado_pieza[6], estado_pieza[7], estado_pieza[8], estado_pieza[9]]
            pieza_centro = Pieza(pieza)
            if not pieza_centro.en_lista(piezas_utilizadas) and not pieza_centro.en_lista(piezas_frontera):
                piezas_frontera.append(pieza_centro)

            #en lado derecho
            pieza = [estado_pieza[0], estado_pieza[1], estado_pieza[3], estado_pieza[2], estado_pieza[5],
                    estado_pieza[4], estado_pieza[7], estado_pieza[6], estado_pieza[9], estado_pieza[8]]
            pieza_derecha = Pieza(pieza)
            if not pieza_derecha.en_lista(piezas_utilizadas) and not pieza_derecha.en_lista(piezas_frontera):
                piezas_frontera.append(pieza_derecha)

            pieza_actual.set_pieza([pieza_izquierda, pieza_centro, pieza_derecha])

#%%
if __name__ == "__main__":
    estado_inicial = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pieza_solucion = rompecabezas_solucion(estado_inicial, solucion)
    #mostrar resultado
    resultado = []
    pieza_actual = pieza_solucion
    while pieza_actual.get_piezas() is not None:
        resultado.append(pieza_actual.get_estado())
        pieza_actual = pieza_actual.get_piezas()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado) 