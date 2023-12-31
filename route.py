import cluster as cl
import utili as ut
import copy

class Route(cl.Cluster):

    def __init__(self):
        super().__init__()
        self.km=0

    def __str__(self):
        stringa = "Route:{" + "km: " + str(self.km)
        for el in self.get_nodi():
            stringa = stringa + '\n' +str(el)
        stringa = stringa + '}'
        return stringa
         
    
    def get_km(self):
        return copy.deepcopy(self.km)
    
    def set_km2(self, km):
        self.km=km

    def set_km(self):
        distanza = 0
        lista = self.get_nodi()
        for i in range(0, len(lista)-1):
            distanza = distanza + ut.distanza(self.get_nodi()[i], self.get_nodi()[i+1])
        self.km=distanza

    def __lt__(self, other):
        return self.km < other.km
    
    def __gt__(self, other):
        return self.km > other.km
    
    def __eq__(self, other):
        return self.km==other.km
