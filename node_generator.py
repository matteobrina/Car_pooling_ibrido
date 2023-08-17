import nodo
from random import randint
def generator():
    x= randint(1, 1000)
    y= randint(1, 1000)
    n=nodo.Nodo(x, y)
    prob = randint(1, 10)
    if (prob < 8):
        n.set_c(1)
    else: 
        n.set_c(5)
    return n

def genera_lista():
    uni = nodo.Nodo(540, 320, 0, 1)
    lista = [uni]
    for i in range(2, 51):
        n=generator()
        n.set_id(i)
        while(n in lista):
            n=generator()
            n.set_id(i)
        lista.append(n)
    return lista



     


