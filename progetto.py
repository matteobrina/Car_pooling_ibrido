import nodo
import cluster_first as cf
import cheapest_insertion as ci
import pickle
import copy
import grafico as gf



"""lista1 = ng.genera_lista()
for el in lista1:
    print(el)
with open('nodi.dat', 'wb') as f:
    pickle.dump(lista1, f)


lista2 = fg.genera_lista()
for el in lista2:
    print(el)
with open('fermate.dat', 'wb') as f:
    pickle.dump(lista2, f)"""

unife = nodo.Nodo(321, 765)


with open('nodi.dat', 'rb') as f:
    lista1 = pickle.load(f)
for el in lista1:
    print(el)

with open('fermate.dat', 'rb') as f:
    lista2 = pickle.load(f)
for el in lista2:
    print(el)

cluster= cf.Cluster_set(copy.deepcopy(lista1), copy.deepcopy(unife), copy.deepcopy(lista2))
for el in cluster.get_cluster_set():
    print(el)
    print(ci.routing(el))

gf.grafico(lista1, lista2, cluster, "figura.png")





















