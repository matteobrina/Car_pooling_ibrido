import nodo
import cluster_first as cf
import cheapest_insertion as ci
import pickle
import copy
import grafico as gf
import local_search as ls


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
cluster2 = copy.deepcopy(cluster)
cluster3=copy.deepcopy(cluster)
for el in cluster.get_cluster_set():
    print(el)
    print(ci.routing(el))

gf.grafico(lista1, lista2, cluster2, "figura.png")

for el in cluster3.get_cluster_set():
    for el2 in ls.due_opt(ci.routing(el)):
        print(el2)

