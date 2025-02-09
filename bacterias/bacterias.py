from numpy import random

def nuevaGeneracion(anteriorGeneracion, tazaCrecimiento):
    nueva = 0
    for i in range(anteriorGeneracion):
        nueva += random.randint(tazaCrecimiento)
    return nueva

def generaciones(bacteriasIniciales,iteraciones):
    bacterias = [bacteriasIniciales]
    for i in range(iteraciones):
        if(bacterias[-1] != 0):
            bacterias.append(nuevaGeneracion(bacterias[-1],4))
        else:
            break
    print(bacterias)

generaciones(10,30)


