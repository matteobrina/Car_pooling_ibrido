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

cluster= cf.Cluster_set(copy.deepcopy(lista1), copy.deepcopy(unife), copy.deepcopy(lista2))
cluster2 = copy.deepcopy(cluster)
for el in cluster.get_cluster_set():
    print(el)
    print(ci.routing(el))

#inizio grafico
plt.figure(figsize=(30, 30))
plt.grid()
plt.xticks(range(0, 1001, 50))
plt.yticks(range(0, 1001, 50))



for el in lista1:
    plt.plot(el.get_x(), el.get_y(), color='pink', marker='o')
    plt.annotate(el.get_id(), (el.get_x(), el.get_y()), textcoords="offset points", xytext=(0,10), ha='center')



for el in cluster2.get_cluster_set():
    route=ci.routing(el)
    lista=route.get_nodi()
    lista_x=[]
    lista_y=[]
    lista_i=[]
    for el2 in lista:
        lista_x.append(el2.get_x())
        lista_y.append(el2.get_y())
        lista_i.append(el2.get_id())
    plt.plot(lista_x, lista_y, color='blue', marker='o', linewidth=0.5)
    for i, label in enumerate(lista_i):
        plt.annotate(label, (lista_x[i], lista_y[i]), textcoords="offset points", xytext=(0,10), ha='center')

for el in lista2:
    plt.plot(el.get_x(), el.get_y(), color='orange', marker='o')
    plt.annotate(el.get_l(), (el.get_x(), el.get_y()), textcoords="offset points", xytext=(10,0), ha='center')

plt.plot(321, 765, color='red', marker='o')

plt.savefig("figura.png")

#fine grafico



















