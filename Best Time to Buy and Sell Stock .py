
# problem statement: Best Time to Buy and Sell Stock (at most one transaction allowed)

# Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed.

# Note: Stock must be bought before being sold.

# Examples:

# Input: prices[] = {7, 1, 5, 3, 6, 4}
# Output: 5
# Explanation:
# The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is witnessed on the 5th day, i.e. price = 6. 
# Therefore, maximum possible profit = 6 – 1 = 5. 

# Input: prices[] = {7, 6, 4, 3, 1} 
# Output: 0
# Explanation: Since the array is in decreasing order, no possible way exists to solve the problem.

def stockDiff(arr):
    l = len(arr)
    small = arr[0]
    index = 0
    
    for i in range(1,l):
        if small > arr[i]:
            small = arr[i]
            index = i
            
    large = small
    for j in range(index, l):
        if large < arr[j]:
            large = arr[j]
    return large - small

arr = [7, 1, 5, 3, 6, 4]
print(stockDiff(arr))