import route as rt

def due_opt(route):
    routes =[]
    if len(route.get_nodi()) <4:
        routes.append(route)
    else:
        for i in range(1, len(route.get_nodi())-2):
            routes.extend(generate_routes_2opt(route, i))
        for el in routes:
            el.set_km()
    return routes

def generate_routes_2opt(route, i):
    r1=[]
    for j in range(i+1, len(route.get_nodi())-1):
        r1.append(swap_2opt(route, i, j))
    return r1

def swap_2opt(route, i, j):
    r1=rt.Route()
    for k in range(0, i):
        r1.aggiungi_nodo(route.get_nodi()[k])
    for z in range(j, i-1, -1):
        r1.aggiungi_nodo(route.get_nodi()[z])
    for t in range(j+1, len(route.get_nodi())):
        r1.aggiungi_nodo(route.get_nodi()[t])
    return r1



