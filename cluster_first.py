from operator import attrgetter
import cluster as cl
import nodo as nd
import utili as ut
class Cluster_set:
    def __init__(self, lista_nodi, unife, lista_fermate):
        set = []
        lista_nodi.sort(key= attrgetter('c'))
        lista_nodi.reverse()
        while(len(lista_nodi)!=0):
            temp_cluster=self.create_cluster(lista_nodi, unife, lista_fermate)
            set.append(temp_cluster)
            for i in range(0, len(temp_cluster.get_nodi())):
                ut.rimuovi(lista_nodi, temp_cluster.get_nodi()[i])
        self.cluster_set=set
        self.number_of_clusters=len(set)

    def create_cluster(self, lista_nodi, unife, lista_fermate):
        cluster = cl.Cluster()
        cluster.aggiungi_nodo(unife)
        starter_node = lista_nodi[0]
        if (starter_node.get_c() == 5):
            s_x = starter_node.get_x()
            s_y = starter_node.get_y()
            u_x = unife.get_x()
            u_y = unife.get_y()
            c=0
            for nodo in lista_nodi:
                if ((nodo.get_c() ==1) and (c<4) and (nodo.get_x() != starter_node.get_x()) and (nodo.get_y() != starter_node.get_y())):
                    if(s_x <= nodo.get_x() and nodo.get_x() <= u_x and s_y <= nodo.get_y() and nodo.get_y() <= u_y or \
                    s_x >= nodo.get_x() and nodo.get_x() >= u_x and s_y <= nodo.get_y() and nodo.get_y() <= u_y or \
                        s_x >= nodo.get_x() and nodo.get_x() >= u_x and s_y >= nodo.get_y() and nodo.get_y() >= u_y or \
                            s_x <= nodo.get_x() and nodo.get_x() <= u_x and s_y >= nodo.get_y() and nodo.get_y() >= u_y):
                        cluster.aggiungi_nodo(nodo)
                        ut.rimuovi(lista_nodi, nodo)
                        c=c+1

            if(c<4):
                for fermata in lista_fermate:
                    if(c<4):
                        if(s_x <= fermata.get_x() and fermata.get_x() <= u_x and s_y <= fermata.get_y() and fermata.get_y() <= u_y or \
                        s_x >= fermata.get_x() and fermata.get_x() >= u_x and s_y <= fermata.get_y() and fermata.get_y() <= u_y or \
                            s_x >= fermata.get_x() and fermata.get_x() >= u_x and s_y >= fermata.get_y() and fermata.get_y() >= u_y or \
                                s_x <= fermata.get_x() and fermata.get_x() <= u_x and s_y >= fermata.get_y() and fermata.get_y() >= u_y):
                        
                            for fermata_collegata in lista_fermate:
                                if((fermata_collegata.get_l()==fermata.get_l()) and (c<4)):
                                    for nodo_p in lista_nodi:
                                        if ((nodo_p.get_c()==1) and (ut.distanza(nodo_p, fermata_collegata)<=50)and (c<4) and (ut.distanza(fermata, fermata_collegata)<ut.distanza(nodo_p, unife))):
                                            nodo_p.set_x(fermata.get_x())
                                            nodo_p.set_y(fermata.get_y())
                                            cluster.aggiungi_nodo(nodo_p)
                                            ut.rimuovi(lista_nodi, nodo_p)
                                            c=c+1 

            cluster.aggiungi_nodo(starter_node)
        
        elif(starter_node.get_c() == 1):
            cluster.aggiungi_nodo(starter_node)
        
        return cluster
    
    def get_cluster_set(self):
        return self.cluster_set
