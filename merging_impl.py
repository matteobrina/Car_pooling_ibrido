import utili as ut
import metaeuristiche_impl as meta
import route as rt
def merge_single_nodes(current_solution, solo_route_list):
    soluzioni=[]
    soluzioni.append(current_solution)
    new_current_solution=ut.copy_routes(current_solution)
    incomplete_route_list=find_incomplete_route(current_solution)
    while(len(solo_route_list)!=0 and len(incomplete_route_list)!=0):
        for route in incomplete_route_list:
            soluzioni.append(merging_single_node(new_current_solution, solo_route_list[0], route))

        solo_route_list.pop(0)
        index=0
        bestkm=ut.kmtot(soluzioni[0])
        for j in range(1, len(soluzioni)):
            if ut.kmtot(soluzioni[j]) < bestkm:
                index=j
                bestkm=ut.kmtot(soluzioni[j])
        
        new_current_solution=ut.copy_routes(soluzioni[index])

        incomplete_route_list.clear()
        incomplete_route_list=find_incomplete_route(new_current_solution)
        
        soluzioni.clear()
        soluzioni.append(new_current_solution)

    return new_current_solution

def merge_incomplete_routes(current_solution):
    possibili_soluzioni=[]
    possibili_soluzioni.append(current_solution)
    new_current_solution=ut.copy_routes(current_solution)
    incomplete_route_list=find_incomplete_route(current_solution)
    not_consider=[]

    while len(incomplete_route_list) >1:
        for i in range(1, len(incomplete_route_list)):
            if (len(incomplete_route_list[0].get_nodi()) + len(incomplete_route_list[i].get_nodi())) <=7:
                possibili_soluzioni.append(merging_incomplete_routes(new_current_solution, incomplete_route_list[0], incomplete_route_list[i]))

        index=0
        best_km=ut.kmtot(possibili_soluzioni[0])
        for j in range(1, len(possibili_soluzioni)):
            if ut.kmtot(possibili_soluzioni[j])<best_km:
                index=j
                best_km=ut.kmtot(possibili_soluzioni[j])

        if index ==0:
            not_consider.append(incomplete_route_list[0])
        
        new_current_solution=ut.copy_routes(possibili_soluzioni[index])
        incomplete_route_list.clear()
        incomplete_route_list=find_incomplete_route(new_current_solution)

        for el in not_consider:
            for el2 in incomplete_route_list:
                if el.get_nodi()[0] in el2.get_nodi():
                    incomplete_route_list.remove(el2)
        
        possibili_soluzioni.clear()
        possibili_soluzioni.append(new_current_solution)

    return new_current_solution

def find_incomplete_route(current_solution):
    incomplete=[]
    for el in current_solution:
        if len(el.get_nodi())==2 and el.get_nodi()[0].get_c()==5:
            incomplete.append(el)
        else:
            if len(el.get_nodi()) >2 and len(el.get_nodi())<6:
                incomplete.append(el)

    return incomplete

def merging_incomplete_routes(current_solution, r1, r2):
    routes=[]
    new_routes=[]
    new_solution=ut.copy_routes(current_solution)
    autisti = []

    for i in range(0, len(r1.get_nodi())):
        if r1.get_nodi()[i].get_c()==5:
            autisti.append(r1.get_nodi()[i])
    
    for i in range(0, len(r2.get_nodi())):
        if r2.get_nodi()[i].get_c()==5:
            autisti.append(r2.get_nodi()[i])
    
    for i in range(0, len(autisti)):
        routes.append(make_route(autisti[i], r1, r2))

    for i in range(0, len(routes)):
        new_routes.append(meta.variable_neighborhood_descend(routes[i]))
    
    for el in new_solution:
        if r1.get_nodi()[0] in el.get_nodi():
            new_solution.remove(el)
    for el in new_solution:
        if r2.get_nodi()[0] in el.get_nodi():
            new_solution.remove(el)

    best_km=new_routes[0].get_km()
    index=0
    for i in range(1, len(new_routes)):
        if new_routes[i].get_km() < best_km:
            index=i
            best_km = new_routes[i].get_km()
    
    new_solution.append(new_routes[index])
    return new_solution

def merging_single_node(current_solution, solo, incomplete):
    new_route = rt.Route()
    new_solution=ut.copy_routes(current_solution)
    new_route.aggiungi_nodo(incomplete.get_nodi()[0])
    new_route.aggiungi_nodo(solo.get_nodi()[0])
    for j in range(1, len(incomplete.get_nodi())):
        new_route.aggiungi_nodo(incomplete.get_nodi()[j])
    new_route_vnd=meta.variable_neighborhood_descend(new_route)
    for el in new_solution:
        if solo.get_nodi()[0] in el.get_nodi():
            new_solution.remove(el)
    for el in new_solution:
        if incomplete.get_nodi()[0] in el.get_nodi():
            new_solution.remove(el)
    new_solution.append(new_route_vnd)
    return new_solution

def make_route(autista, r1, r2):
    route = rt.Route()
    route.aggiungi_nodo(autista)
    if ((len(r1.get_nodi())-1) + len(r2.get_nodi())) <=6:
        for i in range(0, len(r1.get_nodi())-1):
            if r1.get_nodi()[i].get_id() != autista.get_id():
                route.aggiungi_nodo(r1.get_nodi()[i])
        for i in range(0, len(r2.get_nodi())):
            if r2.get_nodi()[i].get_id() != autista.get_id():
                route.aggiungi_nodo(r2.get_nodi()[i])
    route.set_km()
    return route

        