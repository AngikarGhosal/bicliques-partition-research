from IPython import embed

'''
all_bicliques=['1 2 4 5 <-> 10 11 13 14','2 5 <-> 10 11 13 14 12 15','5 <-> 10 11 13 14 12 15 16 17 18','4 5 <-> 10 11 13 14 16 17',
'1 2 3 4 5 6 <-> 11 14','2 3 5 6 <-> 11 14 12 15','5 6 <-> 11 14 12 15 17 18','4 5 6 <-> 11 14 17','1 2 4 5 7 8 <-> 13 14','2 5 8 <-> 13 14 15',
'5 8 <-> 13 14 15 16 17 18','4 5 7 8 <-> 13 14 16 17','1 2 3 4 5 6 7 8 9 <-> 14','2 3 5 6 8 9 <-> 14 15','5 6 8 9 <-> 14 15 17 18',
'4 5 6 7 8 9 <-> 14 17']
'''

with open("all_bicliques_inclusion.txt") as file:
    all_bicliques = file.readlines()
    all_bicliques = [line.rstrip() for line in all_bicliques]

def obtain_set_of_unique_edges(list_of_biclique_tuples):
    Unique_Edges_Set=set()
    for biclique_tuple in list_of_biclique_tuples:
        set_of_edge_tuples=obtain_set_of_edges_from_biclique(*biclique_tuple)
        for x in set_of_edge_tuples:
            Unique_Edges_Set.add(x)
    return Unique_Edges_Set


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

X=obtain_all_tuples_of_nodes(all_bicliques)
Edges=list(obtain_set_of_unique_edges(X))


BicliqueSet=list(obtain_all_bicliques(X))


M=[[0 for i in range(len(BicliqueSet))] for j in range(len(Edges))]

for i in range(len(BicliqueSet)):
    List_of_Edges=list(obtain_set_of_edges_from_biclique(*(BicliqueSet[i])))
    L0=BicliqueSet[i][0].split(" ")
    L1=BicliqueSet[i][1].split(" ")
    for edge in List_of_Edges:
        edge_position=Edges.index(edge)
        ##Sanity Check
        if edge!=Edges[edge_position]:
            print("FALSE")
        if edge[0] not in L0:
            print(edge, L0, "L0")
        if edge[1] not in L1:
            print(edge, L1, "L1")
        #Outputs Nothing
        if edge[0] in L0 and edge[1] in L1:
            M[edge_position][i]=1

ConstraintList=[]
for i in range(len(Edges)):
    print("New Edge", Edges[i])
    ConstraintLine=M[i]
    Constraint='subject to Con'+str(i+1)+': '
    for j in range(len(BicliqueSet)):
        if M[i][j]==1:
            Constraint=Constraint+'x['+str(j+1)+']+'
            if j<60:
                print("J=", j, BicliqueSet[j], "CONTAINS", "I=", i, Edges[i])
    Constraint=Constraint[:len(Constraint)-1]
    Constraint=Constraint+'=1;'
    ConstraintList.append(Constraint)
    print(Constraint[:50])
    print(Constraint[len(Constraint)-20:])
    print()

with open("constraintfile.txt", "w") as f:
    for line in ConstraintList:
        f.write(f"{line}\n")


with open("bicliques.txt", "w") as g:
    for biclique in BicliqueSet:
        x=biclique[0]+' <-> '+biclique[1]
        g.write(f"{x}\n")

with open("edges.txt", "w") as h:
    for edge in Edges:
        x=edge[0]+' <-> '+edge[1]
        h.write(f"{x}\n")

embed()

