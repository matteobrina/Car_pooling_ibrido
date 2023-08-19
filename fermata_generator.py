import fermata
from random import randint
import utili as ut
def generator():
    x= randint(1, 1000)
    y= randint(1, 1000)
    l=randint(1, 6)
    f=fermata.Fermata(x, y, l)
    return f

def genera_lista():
    lista = []
    for i in range(0, 50):
        f=generator()
        while(ut.is_present(lista, f)):
            f=generator()
        lista.append(f)
    return lista
