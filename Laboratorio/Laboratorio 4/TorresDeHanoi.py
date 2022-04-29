#%%
from time import time

#%%
#definicion de funcion para las torres de Hanoi de manera recursiva
def TorresDeHanoiRecursivamente(n, a, b, c):
    #n es numero de discos
    if n == 1:
        print("Movemos un disco de: "+ a +" a "+ c)
    else:
        TorresDeHanoiRecursivamente(n-1, a, c, b)
        print("Movemos un disco de: "+ a +" a "+ c)
        TorresDeHanoiRecursivamente(n-1, b, a, c)

#%%
#definicion de funcion  para las torres de Hanoi de manera iterativa  
def TorresDeHanoiIterativamente(n, a, b, c):
    #barra_A es la barra origen
    #Barra_B es la barra del centro
    #Barra_C es la barra destino
    barra_A  = [0 for x in range(n)]
    barra_B = [0 for x in range(n)]
    barra_C = [0 for x in range(n)]
    pn = [0 for x in range(n)]
    top = 0
    t = False
    auxiliar = ""
    
    while(n > 0 and t == False):
        while(n > 1):
            top += 1
            pn[top] = n
            barra_A [top] = a
            barra_B[top] = b
            barra_C[top] = c
            n -= 1
            auxiliar = b
            b = c
            c = auxiliar
        print("Mover disco de: " + a +" --> "+ c)
        t = True
        if(top > 0):
            n = pn[top]
            a = barra_A [top]
            c = barra_C[top]
            b = barra_B[top]
            top -= 1
            print("Mover disco de: "+ a +" --> "+c)
            n -= 1
            auxiliar = b
            b = a
            a = auxiliar
            t = False

#%%
if __name__ == "__main__":
    print("Ingrese el numero de discos:")
    n = int(input())
    
    print("\n")

    print ("MANERA RECURSIVA")
    tiempo_inicial_R = time()
    TorresDeHanoiRecursivamente(n, "A", "B", "C")
    tiempo_final_R = time()
    tiempo_total_R = tiempo_final_R - tiempo_inicial_R
    
    print("\n")
    
    print ("MANERA ITERATIVA")
    tiempo_inicial_I = time()
    TorresDeHanoiIterativamente(n, "A", "B", "C")
    tiempo_final_I = time()
    tiempo_total_I = tiempo_final_I - tiempo_inicial_I
    
    print("\n")
    
    print ("Tiempo de demora recursivamente: " + str(tiempo_total_R) + " seg")
    print ("Tiempo de demora iterativamente: " + str(tiempo_total_I) + " seg")