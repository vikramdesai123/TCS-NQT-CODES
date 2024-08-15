# problem statement: Print matrix in zig-zag fashion

# Given a matrix of 2D array of n rows and m columns. 
# Print this matrix in ZIG-ZAG fashion as shown in figure.

    # Example: 
    
    # Input:
    # [[1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]]
    
    # Output: 1 2 4 7 5 3 6 8 9

def Print_matrix_in_zigzag_fashion(matrix, rows, columns):
    arr = [[] for i in range (columns + rows-1)]
    
    for i in range(rows):
        for j in range(columns):
            sum = i+j 
            
            if sum % 2 == 0:
                arr[sum].insert(0,matrix[i][j])
            else:
                arr[sum].append(matrix[i][j])

    result = []
    for sunArr in arr:
        result.extend(sunArr)
    return result



matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
rows = 4 
columns = 4 
          
print(Print_matrix_in_zigzag_fashion(matrix,rows,columns))