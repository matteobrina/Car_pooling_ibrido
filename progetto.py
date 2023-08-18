from operator import attrgetter
import nodo
import node_generator as ng
import cluster as cl
import utili as ut
import route as rt
import fermata as fe
import fermata_generator as fg
import cluster_first as cf


lista= ng.genera_lista()

unife = nodo.Nodo(321, 765)

with open('nodi.txt', 'w') as f:
    for el in lista:
        f.write(str(el)+ '\n')

listaf = fg.genera_lista()

cluster= cf.Cluster_set(lista, unife, listaf)
for el in cluster:
    print(el)






