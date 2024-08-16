# problem statement:Given a matrix and a scalar element k, 
#                   our task is to find out the scalar product of that matrix. 

        # Examples: 
        
        # Input : mat[][] = {{2, 3}
        #                   {5, 4}}
        #         k = 5
        # Output : 10 15 
        #          25 20 
        # We multiply 5 with every element.


def scalar_multiplication_of_matrix(matrix, k):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= k 
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
k = 5
print(scalar_multiplication_of_matrix(matrix, k))