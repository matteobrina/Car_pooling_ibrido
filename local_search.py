import route as rt
#inizio intra-route
# inizio 2opt
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
#fine 2opt


#inzio city swap
def node_swap(route):
    routes=[]
    if len(route.get_nodi()) <4:
        routes.append(route)
    else:
        for i in range(1, len(route.get_nodi())-2):
            routes.extend(generate_routes_node_swap(route, i))
        for el in routes:
            el.set_km()
    return routes

def generate_routes_node_swap(route, i):
    r1=[]
    for j in range(i+1, len(route.get_nodi())-1):
        r1.append(swap_node(route, i, j))
    return r1

def swap_node(route, i, j):
    r1=rt.Route()
    for k in range(0, i):
        r1.aggiungi_nodo(route.get_nodi()[k])
    r1.aggiungi_nodo(route.get_nodi()[j])
    for k in range(len(r1.get_nodi()), j):
        r1.aggiungi_nodo(route.get_nodi()[k])
    r1.aggiungi_nodo(route.get_nodi()[i])
    for k in range(len(r1.get_nodi()), len(route.get_nodi())):
        r1.aggiungi_nodo(route.get_nodi()[k])
    return r1


#fine city swap

#inizio chain relocation

def chain_relocation(route):
    routes = []
    if (len(route.get_nodi()) <5):
        routes.append(route)
    else:
        for i in range (1, len(route.get_nodi())-2):
            for j in range(i+1, len(route.get_nodi())-1):
                routes.extend(generate_routes_chain_relocation(route, i, j))
        for el in routes:
            el.set_km()
    return routes

def generate_routes_chain_relocation(route, i, j):
    r1 = []
    relo_nodes=rt.Route()
    for k in range(i, j+1):
        relo_nodes.aggiungi_nodo(route.get_nodi()[k])
    nodes=rt.Route()
    for k in range(0, i):
        nodes.aggiungi_nodo(route.get_nodi()[k])
    for k in range(j+1, len(route.get_nodi())):
        nodes.aggiungi_nodo(route.get_nodi()[k])
    for k in range(1, len(route.get_nodi())):
        temp=single_chain_relocation(nodes, relo_nodes, k, i)
        if temp.get_km()>0:
            r1.append(temp)
    return r1

def single_chain_relocation(nodes, relo_nodes, k, i):
    r1 = rt.Route()
    for t in range(0, len(nodes.get_nodi())):
        if(t!=k):
            r1.aggiungi_nodo(nodes.get_nodi()[t])
        else:
            if(k!=i):
                for z in range(0, len(relo_nodes.get_nodi())):
                    r1.aggiungi_nodo(relo_nodes.get_nodi()[z])
                r1.aggiungi_nodo(nodes.get_nodi()[t])
                r1.set_km2(1)
            else:
                r1.set_km2(-1)
    return r1
#fine chain relocation


#fine intra route



