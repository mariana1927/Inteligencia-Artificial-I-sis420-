#%%
import heapq
from collections import deque
import random
try:
    from itertools import izip
except ImportError:
    izip = zip

#%%
#empaqueta los datos y las funcionalidades de la cola, para que defina su prioridad
class ColaPrioridadLimitada(object):
    def __init__(self, limite=None, *args):
        self.limite = limite
        #implementa colas multi-productor y/o multi-consumidor
        #útil cuando la información debe intercambiarse de forma segura entre varios subprocesos
        self.queue = list()

    #definicion de funcion que devuelve el valor de self.queue
    def __getitem__(self, val):
        return self.queue[val]

    #definicion de funcion para obtener cuantos elementos hay en la lista
    def __len__(self):
        return len(self.queue)

    #definicion de funcion que agrega nuevos elementos a la lista
    def append(self, x):
        heapq.heappush(self.queue, x)
        if self.limite and len(self.queue) > self.limite:
            self.queue.remove(heapq.nlargest(1, self.queue)[0])

    #definicion de funcion que elimina y retorna un elemento de la lista.
    def pop(self):
        return heapq.heappop(self.queue)

    #definicion de funcion que envia ese mismo objeto dentro de la lista,
    #escaneará la lista y agregará ese mismo objeto y,
    #si hay otros, agrrgara el resto dentro de la lista.
    def extend(self, iterable):
        for x in iterable:
            self.append(x)

    #definicion de funcion que remueve un elemento de la lista
    #elimina todos los elementos en el diccionario.
    def clear(self):
        for x in self:
            self.queue.remove(x)

    #definicion de funcion que se utiliza para eliminar una lista de valores del primer partido
    def remove(self, x):
        self.queue.remove(x)

    #definicion de funcion que ordena la lista
    def sorted(self):
        return heapq.nsmallest(len(self.queue), self.queue)

#%%
#clase que traza o dirige el espacio donde se hace la busqueda (Mapa_Laberinto)
#para usar esta clase se debe aplicar los metodos que son solicitados por el algoritmo de busqueda que vamos a usar
class LaberinroBusqueda(object):
    #cada estado se pertener a un estado del Laberinto y cada accion pertenece al limite/frontera del Laberinto

    #definicion de funcion para crear el objeto de busqueda, se llama automaticamente
    def __init__(self, estado_inicial=None):
        self.estado_inicial = estado_inicial

    #definicion de funcion que devueve las acciones que estan disponibles y que son especificas del Laberinto
    def acciones(self, estado):
        raise NotImplementedError
        #raise para levantar una excepción de cualquier tipo

    #definicion de funcion que devuelve el nuevo estado seguidamente de atribuir una accion a ese estado
    def resultado(self, estado, accion):
        raise NotImplementedError

    #definicion de funcion que devuelve el costo de realizar una accion el siguiente estado a partir del estado inicial
    def costo(self, estado, accion, estado2):
        #El valor devuelto es un numero, ya sea entero o flotante, pero por defecto la funcion devuelve 1.
        return 1

    #definicion de funcion que devuelve un valor verdadeo (true) si es el estado al que se quiere llegar
    #y devuelve un valor falso (false) si no es el estado al que se quiere llegar
    def es_objetivo(self, estado):
        raise NotImplementedError
    
    #definicion de funcuon que devuelve el valor que tiene el estado,
    #puede ser un numero, ya sea entero o flotante
    def valor(self, estado):
        raise NotImplementedError

    #definicion de funcion heuristica donde devuelve el costo aproximado para llegar llegar al objetivo de solucion
    def heuristica(self, estado):
        return 0

    #definicion de funcion donde devuelve una cadena de caracteres de un  estado
    def estado_representacion(self, estado):
        return str(estado)

    #definicion de funcion donde devuelve una cadena de caracteres de una accion
    def accion_representacion(self, accion):
        return str(accion)

#%%
#Nodo para el proceso de busqueda en el laberinto
class NodoBusqueda(object):
    #definicion para crear el nodo, se llama automaticamente
    def __init__(self, estado, padre=None, accion=None, costo=0, problema=None, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo = costo
        self.problema = problema or padre.problema
        self.profundidad = profundidad
    
    #definicion para establecer los sucesores del nodo padre
    def expandir(self, busqueda_local=False):
        nodos_nuevos = []
        for accion in self.problema.acciones(self.estado):
            estado_nuevo = self.problema.resultado(self.estado, accion)
            costo = self.problema.costo(self.estado,
                                     accion,
                                     estado_nuevo)
            fabrica_nodos = self.__class__
            nodos_nuevos.append(fabrica_nodos(estado=estado_nuevo,
                                         padre=None if busqueda_local else self,
                                         problema=self.problema,
                                         accion=accion,
                                         costo=self.costo + costo,
                                         profundidad=self.profundidad + 1))
        return nodos_nuevos

    #definicion de funcion para establecer el camino, es decir establecer las accciones + la lista de los nodos,
    #que se debe recorrer desde donde se encuentra el nodo raiz hasta el nodo actual
    def camino(self):
        nodo = self
        camino = []
        while nodo:
            camino.append((nodo.accion, nodo.estado))
            nodo = nodo.padre
        return list(reversed(camino))

    #definicion de funcion para comparar las instancias de la clase NodoBusqueda
    def __eq__(self, otro):
        return isinstance(otro, NodoBusqueda) and self.estado == otro.estado

    #deficion de funcion para la representacion del estado en el que se encuentra un nodo
    def estado_representacion(self):
        return self.problema.estado_representacion(self.estado)

    #deficion de funcion para la representacion de una accion que puede tomar un nodo
    def accion_representacion(self):
        return self.problema.accion_representacion(self.accion)

    #definicion de funcion para poder volver a recrear el objeto en el mismo estado osea, con los mismos valores
    def __repr__(self):
        return 'Node <%s>' % self.estado_representacion().replace('\n', ' ')

    #definicion de funcion para que el objeto no cambie en su vida útil (resumible)
    #asegura devolver un codigo único para cada objeto,
    #y que se mantenga permanente aunque el estado del objeto cambie
    def __hash__(self):
        return hash((
            self.estado,
            self.padre,
            self.accion,
            self.costo,
            self.profundidad,
        ))

#%%
#Nodo para el proceso de busqueda de una heuristica de manera ordenada
class NodoBusquedaHeuristicaOrdenado(NodoBusqueda):
    #definicion de funcion para crear la heuristica, se llama automaticamente
    def __init__(self, *args, **kwargs):
        super(NodoBusquedaHeuristicaOrdenado, self).__init__(*args, **kwargs)
        self.heuristica = self.problema.heuristica(self.estado)

    #definicion de funcion que describe el menor
    def __lt__(self, otro):
        return self.heuristica < otro.heuristica

#%%
#Nodo para el proceso de busqueda 'A*' de manera ordenada
class NodoBusquedaEstrellaOrdenado(NodoBusquedaHeuristicaOrdenado):
    def __lt__(self, otro):
        return self.heuristica + self.costo < otro.heuristica + otro.costo

#defincion de funcion para establecer la busqueda A* 
def aestrella(problema, busqueda_en_grafo=False, viewer=None):
    #si se decreta que la buesuqeda_en_grafo devuelve un valor verdadero (True),
    #se van a eliminar todas las busquedas que aparezcan repetidas.
        #hay que volver a establecer las funciones: acciones, resultado,
        #es_objeto, costo y la heuristica de la clase LaberinroBusqueda.

    #pero si se decreta que la buesuqeda_en_grafo devuelve un valor falso (False),
    #no se van a eliminar todas las busquedas que aparezcan repetidas.
    
    return _buscar(problema,
                   ColaPrioridadLimitada(),
                   busqueda_en_grafo=busqueda_en_grafo,
                   fabrica_nodos=NodoBusquedaEstrellaOrdenado,
                   reemplazar_grafo_cuando_mejor=True)

#definicion de funcion para una busqueda
def _buscar(problema, frontera, busqueda_en_grafo=False, limite_profundidad=None,
            fabrica_nodos=NodoBusqueda, reemplazar_grafo_cuando_mejor=False):
    memoria = set()
    nodo_inicio = fabrica_nodos(estado=problema.estado_inicial, problema=problema)
    frontera.append(nodo_inicio)

    while frontera:
        nodo = frontera.pop()

        if problema.es_objetivo(nodo.estado):
            return nodo
    
        memoria.add(nodo.estado)

        if limite_profundidad is None or nodo.profundidad < limite_profundidad:
            expandido = nodo.expandir()
    
            for n in expandido:
                if busqueda_en_grafo:
                    otros = [x for x in frontera if x.estado == n.estado]
                    assert len(otros) in (0, 1)
                    if n.estado not in memoria and len(otros) == 0:
                        frontera.append(n)
                    elif reemplazar_grafo_cuando_mejor and len(otros) > 0 and n < otros[0]:
                        frontera.remove(otros[0])
                        frontera.append(n)
                else:
                    frontera.append(n)