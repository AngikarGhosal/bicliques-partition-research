def obtain_set_of_unique_edges(list_of_biclique_tuples):
    Unique_Edges_Set=set()
    for biclique_tuple in list_of_biclique_tuples:
        set_of_edge_tuples=obtain_set_of_edges_from_biclique(*biclique_tuple)
        for x in set_of_edge_tuples:
            Unique_Edges_Set.add(x)
    return Unique_Edges_Set

def check_edge_in_biclique(edge, biclique):
    first_nodes_string=biclique.split("<->")[0].strip()
    second_nodes_string=biclique.split("<->")[1].strip()
    edge_left=edge.split("<->")[0].strip()
    edge_right=edge.split("<->")[1].strip()
    first_nodes_list=first_nodes_string.split(" ")
    second_nodes_list=second_nodes_string.split(" ")
    if edge_left in first_nodes_list and edge_right in second_nodes_list:
        return True
    else:
        return False

def check_edges_not_common(edge1, edge2):
    edge1_left=edge1.split("<->")[0].strip()
    edge1_right=edge1.split("<->")[1].strip()
    edge2_left=edge2.split("<->")[0].strip()
    edge2_right=edge2.split("<->")[1].strip()
    if edge1_left!=edge2_left and edge2_left!=edge2_right:
        return True
    else:
        return False

def remove_bad_vertices(biclique, bad_edge):
    first_nodes_string=biclique.split("<->")[0].strip()
    second_nodes_string=biclique.split("<->")[1].strip()
    edge_left=bad_edge.split("<->")[0].strip()
    edge_right=bad_edge.split("<->")[1].strip()
    first_nodes_list=first_nodes_string.split(" ")
    second_nodes_list=second_nodes_string.split(" ")
    first_nodes_list.remove(edge_left)
    second_nodes_list.remove(edge_right)
    if len(first_nodes_list)==0 or len(second_nodes_list)==0:
        return -1
    new_first_nodes_string=" ".join(first_nodes_list)
    new_second_nodes_string=" ".join(second_nodes_list)
    new_biclique=new_first_nodes_string+" <-> "+new_second_nodes_string
    return new_biclique

def obtain_expand_set_bicliques(biclique_tuple):
    set_of_new_bicliques=set()
    list_of_first_nodes=list_of_nodes_from_string(biclique_tuple[0])
    list_of_second_nodes=list_of_nodes_from_string(biclique_tuple[1])
    list_of_first_lists=[[]]
    list_of_second_lists=[[]]
    for el in list_of_first_nodes:
        list_of_first_lists+= [s+[el] for s in list_of_first_lists]
    for el in list_of_second_nodes:
        list_of_second_lists+=[s+[el] for s in list_of_second_lists]
    list_of_first_lists.remove([])
    list_of_second_lists.remove([])
    for x in list_of_first_lists:
        for y in list_of_second_lists:
            xstr=' '.join(x)
            ystr=' '.join(y)
            set_of_new_bicliques.add((xstr,ystr))
    return set_of_new_bicliques

def obtain_all_bicliques(list_of_biclique_tuples):
    Unique_Bicliques_Set=set()
    for biclique_tuple in list_of_biclique_tuples:
        Biclique_Set=obtain_expand_set_bicliques(biclique_tuple)
        Unique_Bicliques_Set=Unique_Bicliques_Set.union(Biclique_Set)
    return Unique_Bicliques_Set

def obtain_set_of_edges_from_biclique(biclique_first_nodes, biclique_second_nodes):
    set_of_edge_tuples=set()
    list_of_first_nodes=list_of_nodes_from_string(biclique_first_nodes)
    list_of_second_nodes=list_of_nodes_from_string(biclique_second_nodes)
    for i in list_of_first_nodes:
        for j in list_of_second_nodes:
            set_of_edge_tuples.add((i,j))
    return set_of_edge_tuples

def list_of_nodes_from_string(nodes_string):
    list_of_nodes=nodes_string.split(" ")
    return list_of_nodes


def obtain_tuple_of_first_and_second_nodes(biclique):
    first_nodes=biclique.split("<->")[0].strip()
    second_nodes=biclique.split("<->")[1].strip()
    return (first_nodes, second_nodes)

def obtain_all_tuples_of_nodes(list_of_bicliques):
    list_of_all_tuples=[]
    for item in list_of_bicliques:
        list_of_all_tuples.append(obtain_tuple_of_first_and_second_nodes(item))
    return list_of_all_tuples