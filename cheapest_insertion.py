import cluster as cl
import route as rt
import utili as ut

def routing(cluster):
    route=rt.Route()
    if len(cluster.get_nodi())==2:
        route.aggiungi_nodo(cluster.get_nodi()[1])
        route.aggiungi_nodo(cluster.get_nodi()[0])
        route.set_km()

    else:
        for i in range(0, len(cluster.get_nodi())):
            if (cluster.get_nodi()[i].get_c()==5):
                route.aggiungi_nodo(cluster.get_nodi()[i])
                cluster.rimuovi_nodo(cluster.get_nodi()[i])
                break

        for i in range(0, len(cluster.get_nodi())):
            if (cluster.get_nodi()[i].get_c()==0):
                route.aggiungi_nodo(cluster.get_nodi()[i])
                cluster.rimuovi_nodo(cluster.get_nodi()[i])
                break

        while(len(cluster.get_nodi())!=0):
            routes = []
            for nodo in cluster.get_nodi():
                for i in range(1, len(route.get_nodi())):
                    routes.append(ut.gen_route(route, nodo, i))
            for el in routes:
                el.set_km()
            
            distanza= routes[0].get_km()
            id = 0
            for i in range(1, len(routes)):
                if(routes[i].get_km() < distanza):
                    distanza=routes[i].get_km()
                    id=i
            route.set_nodi(routes[id].get_nodi())
            route.set_km2(routes[id].get_km())
            for i in range(0, len(cluster.get_nodi())):
                if cluster.get_nodi()[i] in route.get_nodi():
                    cluster.rimuovi_nodo(cluster.get_nodi()[i])
                    break
    return route

