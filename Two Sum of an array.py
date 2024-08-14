# problem statement:

# Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x. 

# Examples: 

# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: -3 1 --->string format
# Explanation: If we calculate the sum of the output,1 + (-3) = -2

# Input: arr[] = {1, -2, 1, 0, 5}, x = 0
# Output: No


def twoSum(arr,sum):
    l = len(arr)
    for i in range(l-1):
        for j in range(i+1, l):
            if (arr[i] + arr[j]) == sum:
                result = str(arr[i])+ " " + str(arr[j])
                return result
    return "no"

arr = [23,43,6,12,87,9,77]
sum = 86
print(twoSum(arr,sum))
