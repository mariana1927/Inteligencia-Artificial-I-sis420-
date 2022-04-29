#%%
class Pieza:
    #definicion para la creacion del objeto (pieza), que se llama auticamente
    def __init__(self, estado, pieza=None):
        self.estado = estado
        self.pieza = None
        self.piezas = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_pieza(pieza)

    #definicion de funcion para definir el estado de una pieza
    def set_estado(self, estado):
        self.estado = estado

    #definicion de funcion para obtener el estado de una pieza
    def get_estado(self):
        return self.estado

    #definicion de funcion para definir el estado de una primer, segunda, etc... pieza
    def set_pieza(self, pieza):
        self.pieza = pieza
        if self.pieza is not None:
            for s in self.pieza:
                s.piezas = self

    #definicion de funcion para obtener el estado de una primer, segunda, etc... pieza
    def get_pieza(self):
        return self.pieza
    
    #definicion de funcion para definir el estado de todas las piezas
    def set_piezas(self, piezas):
        self.piezas = piezas

    #definicion de funcion para obtener el estado de todas las piezas
    def get_piezas(self):
        return self.piezas
    
    #definicion de funcion para definir la accion que debe realizar una pieza
    def set_accion(self, accion):
        self.piezas = accion

    #definicion de funcion para obtener la accion que debe realizar una pieza
    def get_accion(self):
        return self.accion

    #definicion de funcion para definir las acciones que puede realizar una pieza
    def set_acciones(self, acciones):
        self.acciones = acciones

    #definicion de funcion para obtener las acciones que puede realizar una pieza
    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    #compara las instancias de la clase Pieza
    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    #coloca las piezas en una lista
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    #devuelve un array con las piezas (los 10 dígitos)
    def __str__(self):
        return str(self.get_estado())