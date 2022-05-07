import collections
import itertools

def Phi(g, k,n, labels_map): # add labels_map arg
    
    adj_mat = nx.to_numpy_matrix(g)
    
    all_cliques= nx.enumerate_all_cliques(g)
    
    #all_cliques2 = all_cliques

    k_cliques=[x for x in all_cliques if len(x)== k+1 ]
    
    all_cliques= nx.enumerate_all_cliques(g)
    # must generate simplex of m vertices
    n_cliques = [y for y in all_cliques if len(y) <= n]

    print("k cliques:", k_cliques)
    print("n cliques:", n_cliques)
    # create new graph with vertex set k_cliques

    # map from index to set
    map1 = {}
    map2 = {} # backwards map
    ind1=0
    
    new_labels = {}

    for x in k_cliques:
        print("x is", x)
        xtup = tuple(x)
        map1[ind1] = x         
        map2[xtup] = ind1
        
        # aggregation of labels 
        label_list = []
        for vertex in x:
            vlabel = labels_map[vertex]
            label_list.append(vlabel) # extend(vlabel)
        new_labels[ind1] = label_list
        
        ind1= ind1+1

    adj_mat = np.zeros((ind1,ind1))
    new_edge_list = []

    # check adjacency up to m vertices
    ind1 =0
    ind2 = 0
    for c1 in k_cliques:
        for c2 in k_cliques:
            c1tup = tuple(c1)
            c2tup = tuple(c2)
            index1 = map2[c1tup]
            index2 = map2[c2tup]
            # compare lists for same elements
            if ind1== ind2:#c1 == c2:
                continue
            counter1 = collections.Counter(c1)
            counter2 = collections.Counter(c2)
            set_list1 = set(tuple(d for d in sorted(counter1)))
            set_list2 = set(tuple(d for d in sorted(counter2)))
            intersect = set_list1.intersection(set_list2)
            ilen = len(intersect)
            print("ilen is", ilen)
            
            # check if edge exists between the nodes not the same ; May 7
            distinct = list(set(set_list1).symmetric_difference(set(set_list2)))
            
            distinct_pairs = list(itertools.combinations(distinct, 2)) 
            
            # check if edge exists 
            for p in distinct_pairs:
                p1 = p[0]
                p2 = p[1]
                if adj_mat[p1,p2] == 1: # != 0
                    ilen = ilen+1
            
            # modification to the input of the operator: if there is n=1 or more vertices in common
            if ilen>= n: # n-1 
                # add edge
                adj_mat[index1, index2] = 1
                adj_mat[index2, index1] = 1
                new_edge_list.append((index1, index2))
                new_edge_list.append((index2, index1))
                
                # check & aggregate edge labels ?
                
                
            ind2 = ind2+1
        ind1 = ind1+1
        
        # may 3 
        new_edge_labels = {}

    return adj_mat, new_edge_list, k_cliques, new_labels
