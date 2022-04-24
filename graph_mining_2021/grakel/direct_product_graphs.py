# direct product of graphs

def direct_prod(g1, g2, v_labels1, v_labels2, e_labels1, e_labels2):
    
    n = len(g1)
    
    # first generate vertices (v1,v2) 
    vertices1x2 = {}
    inverse_vertices1x2= {}
    ind=0
    
    v1 = 0
    for lab1 in v_labels1:
        v2 = 0
        for lab2 in v_labels2:
            
            if lab1 == lab2:
                
                pair = (v1, v2)

                vertices1x2[ind] = pair
                inverse_vertices1x2[pair] = ind
            ind= ind+1
            v2 +=1
        v1+=1
            
    
    # iterate over adj matrices and edge lists 
    
    e_labels3 = np.zeros((n,n))
    
    g1_row = 0
    g2_row = 0
    for row1 in g1:
        for row2 in g2: 
            g1_col = 0
            g2_col = 0
            for e1 in row1:
                
                for e2 in row2:
                    
                    # check condition (u_1, u_2) in E1 and (v_1, v_2) in E2 and labele(u_1,u_2) = labele(v_1, v_2)
                    if e1 != 0:
                        if e2!=0:
                            # check label
                            label1 = e_labels1[g1_row, g1_col]
                            label2 = e_labels2[g2_row, g2_col]
                            
                            if label1==label2:
                                # add edge
                                v1 = inverse_vertices1x2[(g1_row, g1_col)]
                                v2 = inverse_vertices1x2[(g2_row, g2_col)]
                                e_labels3[v1, v2] = 1
                    
                    g2_col +=1
                g1_col+=1
            g2_row +=1
        g1_row +=1
                        
                    
# for efficiency, direct product of grouped vertices;



# group together vertices / edges based on closeness

# group together vertices / edges based on min wt cycle basis


# optimal assignment search based on (?) topological similarity


# independent sets based on being farther away from each other; start comparison between different groups

## compute the expander-ness of each group / set to compare 
