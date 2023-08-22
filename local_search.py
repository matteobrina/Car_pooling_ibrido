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

#inizio inter route
#inizio string exchange
def string_exchange(r1, r2):
    routes = []
    if(len(r1.get_nodi())==3):
        routes = string_exchange_3(r1, r2, True)
    else:
        if(len(r2.get_nodi())==3):
            routes=string_exchange_3(r2, r1, False)
        else:
            if((len(r1.get_nodi())>3) and (len(r2.get_nodi())>3)):
                index =0
                for i in range(1, len(r1.get_nodi())-1):
                    for k in range(1, len(r2.get_nodi())-1):
                        routes.insert(index, make_string_exchange(r1, r2, k, i))
                        index = index+1
                for i in range(1, len(r1.get_nodi())-2):
                    for k in range(1, len(r2.get_nodi())-2):
                        routes.insert(index, make_string_exchange_bis(r1, r2, k, i))
                        index=index+1
    return routes

def string_exchange_3(r1, r2, flag):
    routes = []
    n = r1.get_nodi()[1]
    index=0
    for i in range(1, len(r2.get_nodi())-1):
        routes.insert(index, exchange_dim_3(r1, r2, n, i, flag))
        index=index+1
    return routes

def exchange_dim_3(r1, r2, n, i, flag):
    nodes1 = []
    nodes1.append(r2.get_nodi()[i])
    nodes2 = []
    nodes2.append(n)
    r = []
    if flag:
        r.insert(0, make_route_string_exchange(r1, nodes1, 1))
        r.insert(1, make_route_string_exchange(r2, nodes2, i))
    else:
        r.insert(0, make_route_string_exchange(r2, nodes2, i))
        r.insert(1, make_route_string_exchange(r1, nodes1, 1))        
    return r     

def make_string_exchange(r1, r2, k, i):
    r = []
    nodes1 =[]
    nodes2 = []
    nodes1.append(r2.get_nodi()[k])
    nodes2.append(r1.get_nodi()[i])
    r.insert(0, make_route_string_exchange(r1, nodes1, i))
    r.insert(1, make_route_string_exchange(r2, nodes2, k))
    return r

def make_string_exchange_bis(r1, r2, k, i):
    r = []
    nodes1=[]
    nodes2=[]
    nodes1.append(r2.get_nodi()[k])
    nodes1.append(r2.get_nodi()[k+1])

    nodes2.append(r1.get_nodi()[i])
    nodes2.append(r1.get_nodi()[i+1])

    r.insert(0, make_route_string_exchange(r1, nodes1, i))
    r.insert(1, make_route_string_exchange(r2, nodes2, k))
    return r


def make_route_string_exchange(r, nodes, i):
    temp = rt.Route()
    for z in range(0, i):
        temp.aggiungi_nodo(r.get_nodi()[z])
    for el in nodes:
        temp.aggiungi_nodo(el)
    for z in range(len(temp.get_nodi()), len(r.get_nodi())):
        temp.aggiungi_nodo(r.get_nodi()[z])
    temp.set_km()
    return temp


#fine string exchange

#inizio string relocation

def string_relocation(r1, r2):
    routes = []
    if(len(r1.get_nodi())==6 and len(r2.get_nodi())==6):
        r=[]
        r.insert(0, r1)
        r.insert(1, r2)
        routes.append(r)
        return routes
    
    if(len(r1.get_nodi())==6 or len(r2.get_nodi())==6):
        if len(r1.get_nodi())==6:
            routes=string_relo(r1, r2, True)
        else:
            routes=string_relo(r2, r1, False)
    else:
        copy_r1 = rt.Route()
        copy_r2=rt.Route()
        for i in range(0, len(r1.get_nodi())):
            copy_r1.aggiungi_nodo(r1.get_nodi()[i])
        for i in range(0, len(r2.get_nodi())):
            copy_r2.aggiungi_nodo(r2.get_nodi()[i])
        routes=string_relo(r1, r2, True)
        routes.extend(string_relo(copy_r2, copy_r1, False))
    return routes

def string_relo(r1, r2, flag):
    routes = []
    for i in range(1, len(r1.get_nodi())-1):
        for j in range(1, len(r2.get_nodi())):
            routes.append(pos(r1, r2, i, j, flag))
    return routes

def pos(r1, r2, i, j, flag):
    r=[]
    if(flag):
        r.insert(0, remove_node(r1, i))
        r.insert(1, add_node(r2, j, r1.get_nodi()[i]))
    else:
        r.insert(0, add_node(r2, j, r1.get_nodi()[i]))
        r.insert(1, remove_node(r1, i))
    return r

def remove_node(route, i):
    r = rt.Route()
    for j in range(0, i):
        r.aggiungi_nodo(route.get_nodi()[j])
    for j in range(i+1, len(route.get_nodi())):
        r.aggiungi_nodo(route.get_nodi()[j])
    return r

def add_node(route, i, node):
    r = rt.Route()
    for j in range(0, i):
        r.aggiungi_nodo(route.get_nodi()[j])
    r.aggiungi_nodo(node)
    for j in range(i, len(route.get_nodi())):
        r.aggiungi_nodo(route.get_nodi()[j])
    return r

#fine string relocation
#fine inter route



