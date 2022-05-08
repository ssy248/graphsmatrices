# reweight the adjacency matrix by relationship between each pair of vertices
reweighted = reweight(adj_mat)
# normal random walk
def normal_random_walk(reweighted):
  n= len(reweighted)
  new_adj_mat = np.zeros((n,n))
  ind=0
  for row in reweighted:
    row_sum = sum(row)
    new_row = row/(row_sum)
    new_adj_mat[ind] = new_row
  return(new_adj_mat)    

# preferential navigation
def preferential_navigation(A, q, beta):
  n = len(A)
  new_adj_mat = np.zeros((n,n))
  x_ind = 0
  for row in A:
    y_ind=0
    # denominator
    denom = 0
    for el in range(n):
      denom= denom + np.pow(A[x_ind, el], np.pow(q[el],beta))
    for el in row:
      numer_ij = np.matmul(A[x_ind, y_ind], np.pow(q[y_ind], beta))
      p_ij = numer_ij/(denom)
      new_adj_mat[x_ind, y_ind] = p_ij
      y_ind +=1
    x_ind +=1
  return(new_adj_mat)
    
# stationary distribution

# pref navigation random walk
def preferential_navigation_stationary_i(A, q, beta,i):
    n = len(A)
    new_adj_mat = np.zeros((n,n))
    x_ind = 0
    numerator = 0
    for ell in range(n):
        numerator = numerator+ np.pow(q[i]*q[ell], beta)*A[i,ell]
    denominator =0 
    for ell in range(n):
        for m in range(n):
            denominator= denominator+ np.pow(q[ell]*q[m], beta)*A[ell, m]
    return (numerator)/(denominator)


# max entropy random walks

def max_entropy_random_walk_i(eps, i):
    
    return np.pow(eps[i], 2)
