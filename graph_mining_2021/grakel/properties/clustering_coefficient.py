# properties: clustering coefficient (a study of visibility graphs for )

# for any node i, ratio of # of edges btwn its nbrs and # of possible edges

def clustering_coefficient(i, g): # node i in graph g (adj mat)
    # calculate number edges for each vertex
    n_edges=[]
    for row in g:
        n_edges.append(sum(row))
    
    # k_i nbrs 
    row_i = g[i]
    k_i = sum(row_i)
    # E_i : number of edges btwn i's nbrs
    E_i = 0
    ind = 0
    for el in row_i:
        if el== 1:
            n_current = n_edges[ind]
            E_i = E_i + n_current
        ind = ind+1
    C_i = 2*E_i/(k_i*(k_i-1))
    return C_i
