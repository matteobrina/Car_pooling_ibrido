import copy

class Cluster:

    def __init__(self):
        self.nodi=[]

    def __str__(self):
        stringa="Cluster: {"
        for el in self.nodi:
            stringa= stringa+str(el)+ '\n'
        
        stringa=stringa+ '}'

        return stringa
    
    def get_nodi(self):
        return copy.deepcopy(self.nodi)
    
    def set_nodi(self, nodi):
        self.nodi=nodi

    def aggiungi_nodo(self, nodo):
        self.nodi.append(nodo)

    def rimuovi_nodo(self, nodo):
        self.nodi.remove(nodo)

