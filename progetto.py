import nodo
import node_generator as ng
import cluster as cl
import utili as ut
import route as rt


lista= ng.genera_lista()
for el in lista:
    print(el)

with open('nodi.txt', 'w') as f:
    for el in lista:
        f.write(str(el)+ '\n')


nodo1 = nodo.Nodo(1, 2)
nodo2 = nodo.Nodo(3, 4)
nodo3 = nodo.Nodo(5, 6)
route=rt.Route()
route2=rt.Route()
route.aggiungi_nodo(nodo1)
route.aggiungi_nodo(nodo2)
route.aggiungi_nodo(nodo3)
route2.aggiungi_nodo(nodo1)
route2.aggiungi_nodo(nodo2)
route2.aggiungi_nodo(nodo3)
route.set_km()
route2.set_km()
listaaaa= [route, route2]
print(str(ut.kmtot(listaaaa)))
print(str(route))

