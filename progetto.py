from operator import attrgetter
import nodo
import node_generator as ng
import cluster as cl
import utili as ut
import route as rt
import fermata as fe
import fermata_generator as fg
import cluster_first as cf
import cheapest_insertion as ci
import pickle
import matplotlib.pyplot as plt


"""lista= ng.genera_lista()
for el in lista:
    print(el)

unife = nodo.Nodo(321, 765)

with open('nodi.txt', 'w') as f:
    for el in lista:
        f.write(str(el)+ '\n')

listaf = fg.genera_lista()
for el in listaf:
    print(el)


cluster= cf.Cluster_set(lista, unife, listaf)
for el in cluster.get_cluster_set():
    print(el)
    print(ci.routing(el))"""



unife = nodo.Nodo(321, 765)
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

with open('nodi.dat', 'rb') as f:
    lista1 = pickle.load(f)
for el in lista1:
    print(el)

with open('fermate.dat', 'rb') as f:
    lista2 = pickle.load(f)
for el in lista2:
    print(el)

cluster= cf.Cluster_set(lista1, unife, lista2)
for el in cluster.get_cluster_set():
    print(el)
    print(ci.routing(el))



















