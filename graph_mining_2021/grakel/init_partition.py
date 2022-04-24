# partition them by searching for leaves (degree 1 ) and vertices of degree 2 , slowly adding their neighbors to the group 

deg1v = []
deg2v = []
ind=0
for row in adj_mat:
	deg_row = sum(row)
	if deg_row==1:
		deg1v.append(ind)
	if deg_row==2:
		deg2v.append(ind)  	
	
	ind=ind+1
