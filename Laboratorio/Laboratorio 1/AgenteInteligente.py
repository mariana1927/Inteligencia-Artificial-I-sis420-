#%%
ACCIONES = {
    'plaga':'pedir_coordenada',
    'plaga,p1':'plaga1_exterminada',
    'plaga,p2':'plaga2_exterminada',
    'plaga,p3':'plaga3_exterminada',
    'plaga,p1,plaga':'pedir_coordenada',
    'plaga,p2,plaga':'pedir_coordenada',
    'plaga,p3,plaga':'pedir_coordenada',
    'plaga,p1,plaga,p1':'plaga1_exterminada',
    'plaga,p1,plaga,p2':'plaga2_exterminada',
    'plaga,p1,plaga,p3':'plaga3_exterminada',
    'plaga,p2,plaga,p1':'plaga1_exterminada',
    'plaga,p2,plaga,p2':'plaga2_exterminada',
    'plaga,p2,plaga,p3':'plaga3_exterminada',
    'plaga,p3,plaga,p1':'plaga1_exterminada',
    'plaga,p3,plaga,p2':'plaga2_exterminada',
    'plaga,p3,plaga,p3':'plaga3_exterminada'
    }

#%%
class AgenteRobot:
    def __init__(self, acciones):
        self.acciones = acciones
        self.percepciones = ""

    def actuar(self, percepsion, accion_basica=''):
        if not percepcion:
            return accion_basica
        if len(self.percepciones) !=0:
            self.percepciones += ","
        self.percepciones += percepcion
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones = ''
        return accion_basica

#%%
print("ROBOT ESPANTA PLAGAS")
expendedora = AgenteRobot(ACCIONES)
percepcion = input("Indicar percepcion: ")
while percepcion:
    accion = expendedora.actuar(percepcion, 'esperar')
    print(accion)
    percepcion = input("Indicar percepcion: ")