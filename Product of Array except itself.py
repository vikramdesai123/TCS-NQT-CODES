    # problem statement: Product of Array except itself

# Given an array arr[] of n integers, construct a Product Array prod[] (of the same size) such that 
# prod[i] is equal to the product of all the elements of arr[] except arr[i]. 

    # Input: arr[]  = {10, 3, 5, 6, 2}
    # Output: prod[]  = {180, 600, 360, 300, 900}
    # 3 * 5 * 6 * 2 product of other array 
    # elements except 10 is 180
    # 10 * 5 * 6 * 2 product of other array 
    # elements except 3 is 600
    # 10 * 3 * 6 * 2 product of other array 
    # elements except 5 is 360
    # 10 * 3 * 5 * 2 product of other array 
    # elements except 6 is 300
    # 10 * 3 * 6 * 5 product of other array 
    # elements except 2 is 900


def arrElementMultiplication(arr):
    product = []
    for i in range(len(arr)):
        mult = 1 
        for j in range(len(arr)):
            if i != j:
                mult *= arr[j]
        product.append(mult)
    return product

arr = [10, 3, 5, 6, 2]
print(arrElementMultiplication(arr))