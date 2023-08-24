import node_generator as ng
import pickle
import fermata_generator as fg
lista1 = ng.genera_lista()
for el in lista1:
    print(el)
with open('nodi.dat', 'wb') as f:
    pickle.dump(lista1, f)


lista2 = fg.genera_lista()
for el in lista2:
    print(el)
with open('fermate.dat', 'wb') as f:
    pickle.dump(lista2, f)
