import nodo
import cluster_first as cf
import cheapest_insertion as ci
import pickle
import copy
import grafico as gf
import local_search as ls
import metaeuristiche_impl as meta
import utili as ut
import merging_impl as mer

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
lista_di_cluster=cluster.get_cluster_set()
lista_di_routes=[]
for el in lista_di_cluster:
    lista_di_routes.append(ci.routing(el))

"""stringa = ls.string_relocation
print("\n INIZIO COPPIE")
for i in range(0, len(cluster.get_cluster_set())):
    print('\n')
    print('\n')
    for k in range(i+1, len(cluster.get_cluster_set())):
        if(k!=i):
            print('\n')
            for el in stringa(ci.routing(cluster.get_cluster_set()[i]), ci.routing(cluster.get_cluster_set()[k])):
                print("ELEMENTO1"+str(el[0]) + "\n ELEMENTO2"+ str(el[1]))"""


"""for el in lista_di_routes:
    nuove_routes.append(meta.variable_neighborhood_descend(el))"""
nuove_routes=copy.deepcopy(lista_di_routes)
routes2=copy.deepcopy(lista_di_routes)
routes3 = copy.deepcopy(lista_di_routes)
solo_routes = []
for el in routes2:
    if len(el.get_nodi())==2:
        solo_routes.append(el)

routes_merge1=mer.merge_single_nodes(routes2, solo_routes)
print("ROUTES CON PRIMO MERGE")
for el in routes_merge1:
    print(el)


gf.grafico2(lista1, lista2, routes_merge1, 'figura2.png')

routes_merge2= mer.merge_incomplete_routes(routes_merge1)
print("ROUTES CON SECONDO MERGE")
for el in routes_merge2:
    print(el)


gf.grafico2(lista1, lista2, routes_merge2, 'figura3.png')

lista_finale = copy.deepcopy(routes_merge2)




for i in range(0, len(lista_finale)):
    for k in range(i+1, len(lista_finale)):
        temp=meta.variable_neighborhood_search(lista_finale[i], lista_finale[k])
        if(ut.kmtot(temp)<(lista_finale[i].get_km()+lista_finale[k].get_km())):
            lista_finale[i]=temp[0]
            lista_finale[k]=temp[1]

for el in lista_finale:
    print(str(el))

print("totale km vecchie routes:    "+str(ut.kmtot(nuove_routes)))
print("totale km merging1:    "+str(ut.kmtot(routes_merge1)))
print("totale km merging2:    "+str(ut.kmtot(routes_merge2)))
print("totale km nuove routes:    "+ str(ut.kmtot(lista_finale)))

gf.grafico2(lista1, lista2, lista_finale, 'figura4.png')


