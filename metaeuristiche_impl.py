import utili as ut
import configuration as conf
import random as ra
def variable_neighborhood_search(r1, r2, k):
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
    try:
        while True:
            number_of_neighbor=0
            dim_init_sol=ut.kmtot(routes_optimized[0])
            while number_of_neighbor < len(conf.inter_route):
                funzione=conf.inter_route[number_of_neighbor]
                routes=funzione(route1, route2)
                shake= ra.randint(0, len(routes))
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
                routes_optimized.extend(r)
                dim_sol_trovata=ut.kmtot(routes_optimized[0])
            iter=iter+1

            if iter >= max_iterations:
                break

        solution.append(route1)
        solution.append(route2)
        return solution
    except:
        solution.append(r1)
        solution.append(r2)

        return solution
    

def vnd(r1, r2):
    routes=[]
    routes.append(variable_neighborhood_descend(r1))
    routes.append(variable_neighborhood_descend(r2))
    return routes


            



    