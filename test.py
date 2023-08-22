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
for el in cluster.get_cluster_set():
    print(el)
    print(ci.routing(el))

"""print("\n INIZIO COPPIE")
for i in range(0, len(cluster.get_cluster_set())):
    print('\n')
    print('\n')
    for k in range(i+1, len(cluster.get_cluster_set())):
        if(k!=i):
            print('\n')
            for el in ls.string_exchange(ci.routing(cluster.get_cluster_set()[i]), ci.routing(cluster.get_cluster_set()[k])):
                print("ELEMENTO1"+str(el[0]) + "\n ELEMENTO2"+ str(el[1]))"""

stringa = ls.string_relocation
print("\n INIZIO COPPIE")
for i in range(0, len(cluster.get_cluster_set())):
    print('\n')
    print('\n')
    for k in range(i+1, len(cluster.get_cluster_set())):
        if(k!=i):
            print('\n')
            for el in stringa(ci.routing(cluster.get_cluster_set()[i]), ci.routing(cluster.get_cluster_set()[k])):
                print("ELEMENTO1"+str(el[0]) + "\n ELEMENTO2"+ str(el[1]))

