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


lista= ng.genera_lista()
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
    print(ci.routing(el))










