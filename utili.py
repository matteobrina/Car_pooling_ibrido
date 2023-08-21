import nodo
import math
import route as rt

def distanza(nodo1, nodo2):
    return math.sqrt(pow(nodo2.get_x()-nodo1.get_x(), 2)+ pow(nodo2.get_y()-nodo1.get_y(), 2))

def rimuovi(lista, nodo):
    for el in lista:
        if (nodo.get_id() == el.get_id()):
            lista.remove(nodo)

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

def gen_route(route, nodo, indice):
    route2 = rt.Route()
    lista=route.get_nodi()
    lista.insert(indice, nodo)
    route2.set_nodi(lista)
    return route2

