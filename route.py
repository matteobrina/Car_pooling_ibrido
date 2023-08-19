import cluster as cl
import utili as ut

class Route(cl.Cluster):

    def __str__(self):
        return "Route:{" + "km: " + str(self.km) + '}' 
    
    def get_km(self):
        return self.km
    
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
