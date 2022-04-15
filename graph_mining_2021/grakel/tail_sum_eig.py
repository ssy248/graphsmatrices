# calculate the tail sum of eigenvalues of kernel matrix

def tail_sum_eig(kmatrix, n): # n eigenvalues from tail 
    
    eigs, evecs = linalg.eig(kmatrix)
    
    # sort them 
    eig_sorted = np.sort(eigs)
    
    tot_len = len(eigs)
    tot_len_minus_n = tot_len - n
    # sum the tail
    eig_tail = eig_sorted[tot_len_minus_n: tot_len]
    
    return(sum(eig_tail))

# operate on boolean addition/ product  of matrices
