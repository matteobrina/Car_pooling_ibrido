import nodo
import math

def distanza(nodo1, nodo2):
    return math.sqrt(pow(nodo2.x-nodo1.x, 2)+ pow(nodo2.y-nodo1.y, 2))

def rimuovi(lista, nodo):
    for el in lista:
        if nodo.i == el.i:
            lista.remove(el)

def kmtot(lista):
    tot = 0
    for el in lista:
        tot = tot+ el.get_km()
    return tot

