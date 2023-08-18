import nodo
import math

def distanza(nodo1, nodo2):
    return math.sqrt(pow(nodo2.get_x()-nodo1.get_x(), 2)+ pow(nodo2.get_y()-nodo1.get_y(), 2))

def rimuovi(lista, nodo):
    for el in lista:
        if nodo.get_id() == el.get_id():
            lista.remove(el)

def kmtot(lista):
    tot = 0
    for el in lista:
        tot = tot+ el.get_km()
    return tot

def is_present(lista, nodo):
    for el in lista:
        if((el.get_x() == nodo.get_x()) and (el.get_y()==nodo.get_y())):
            return True
    return False

