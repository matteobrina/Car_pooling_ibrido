import utili as ut
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
        
        