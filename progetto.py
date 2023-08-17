import nodo
import node_generator as ng

lista= ng.genera_lista()
for el in lista:
    print(el)

with open('nodi.txt', 'w') as f:
    for el in lista:
        f.write(str(el)+ '\n')



