import utili as ut
import configuration as conf
import random as ra
import route as rt
from operator import attrgetter
def variable_neighborhood_search(r1, r2):
    iter=0
    max_iterations=5
    routes=[]
    r=[]
    r.append(r1)
    r.append(r2)
    routes_optimized=[]
    routes_optimized.append(r)
    dim_sol_trovata=0
    route1=r1
    route2=r2
    solution=[]
    
    while True:
        number_of_neighbor=0
        #dim_init_sol=ut.kmtot(routes_optimized[0])
        while number_of_neighbor < len(conf.inter_route):
            funzione=conf.inter_route[number_of_neighbor]
            routes=funzione(route1, route2)
            if len(routes)==0:
                break
            if(len(routes)==1):
                route1primo=routes[0][0]
                route2primo=routes[0][1]
            else:
                shake= ra.randint(0, len(routes)-1)
                route1primo=routes[shake][0]
                route2primo=routes[shake][1]
            routes.clear()
            routes=funzione(route1primo, route2primo)
            for i in range(0, len(routes)):
                routes_optimized.append(vnd(routes[i][0], routes[i][1]))
            index=0
            best_km=ut.kmtot(routes_optimized[0])
            for j in range(1, len(routes_optimized)):
                if ut.kmtot(routes_optimized[j])<best_km:
                    index=j
                    best_km=ut.kmtot(routes_optimized[j])
            if index==0:
                number_of_neighbor=number_of_neighbor+1
            else:
                number_of_neighbor=0
            
            route1=routes_optimized[index][0]
            route2=routes_optimized[index][1]
            routes_optimized.clear()
            r.clear()
            r.append(route1)
            r.append(route2)
            routes_optimized.append(r)
            #dim_sol_trovata=ut.kmtot(routes_optimized[0])
        iter=iter+1

        if iter >= max_iterations:
            break

    solution.append(route1)
    solution.append(route2)
    return solution
    
    

def vnd(r1, r2):
    routes=[]
    routes.append(variable_neighborhood_descend(r1))
    routes.append(variable_neighborhood_descend(r2))
    return routes

def variable_neighborhood_descend(init_sol):
    intorno = []
    current_solution = rt.Route()
    for j in range(0, len(init_sol.get_nodi())):
        current_solution.aggiungi_nodo(init_sol.get_nodi()[j])
    current_solution.set_km()
    number_of_neighbor=0

   
    while number_of_neighbor < len(conf.intra_route):
        intorno=conf.intra_route[number_of_neighbor](current_solution)
        for j in range(0, len(intorno)):
            intorno[j].set_km()
        intorno.sort(key=attrgetter('km'))
        if intorno[0].get_km() >= current_solution.get_km():
            number_of_neighbor = number_of_neighbor+1
        else:
            current_solution.get_nodi_rif().clear()
            for j in range(0, len(intorno[0].get_nodi())):
                current_solution.aggiungi_nodo(intorno[0].get_nodi()[j])
            current_solution.set_km()
            number_of_neighbor=0
    return current_solution
    
    
    



            



    