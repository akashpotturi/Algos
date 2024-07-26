def shortest_distance(self, matrix):
		n = len(matrix)
		#matrix[i][j] == -1 if there is no edge between i and j
		for i in range(n):
		    for j in range(n):
		        if matrix[i][j] == -1:
		            matrix[i][j] = 10**9
		for k in range(n):
		    for i in range(n):
		        for j in range(n):
		            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
		for i in range(n):
		    for j in range(n):
		        if matrix[i][j]>=10**9:
		            matrix[i][j] = -1
		return matrix
