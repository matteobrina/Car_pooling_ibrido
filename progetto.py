import nodo
import node_generator as ng
import fermata_generator as fg
import cluster_first as cf
import cheapest_insertion as ci
import pickle
import matplotlib.pyplot as plt
import copy



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

cluster= cf.Cluster_set(lista1, unife, lista2)
cluster2 = copy.deepcopy(cluster)
for el in cluster.get_cluster_set():
    print(el)
    print(ci.routing(el))

plt.figure()
for el in cluster2.get_cluster_set():
    route=ci.routing(el)
    lista=route.get_nodi()
    lista_x=[]
    lista_y=[]
    for el2 in lista:
        lista_x.append(el2.get_x())
        lista_y.append(el2.get_y())
    plt.plot(lista_x, lista_y, color='blue', marker='o')


plt.savefig("figura.png")



















