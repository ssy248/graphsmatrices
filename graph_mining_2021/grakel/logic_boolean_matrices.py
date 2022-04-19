# logic of boolean matrices operations A_1 in R^(q_1 x q_2)  and A_2 in R^(q_2 x q_3)

# product: (i,j) entry of A_1 x A_2 is  max_{k in [1,q_2]} min (a_{1,i,k}, a_{2, k,j})

q1 = a1.shape[0]
q2 = a1.shape[1]
q3 = a2.shape[1]

a1_times_a2 = np.zeros((q1, q3))

for i in range(q1):
    for j in range(q3):
        # array
        temp_array = []
        for k in range(q2):
            temp1 = a1[i,k] # a_{1,i,k}
            temp2 = a2[k,j] # a_{2, k,j}
            temp_array.append(min(temp1, temp2))
        # find the max over k
        temp_max = max(temp_array)
        a1_times_a2[i,j] = temp_max

# mat addition operation; A_1, A_2 in R^(q1 x q2)

# (i,j) entry is max(a_{1,i,j}, a_{2, i, j})


a1_plus_a2 = np.zeros((q1, q2))

for i in range(q1):
    for j in range(q2):
        temp = max(a1[i,j], a2[i,j])
        a1_plus_a2[i,j] = temp
        
