# Problem Statement

# Particulate matters are the biggest contributors to Delhi pollution. The main reason behind the increase in the concentration of PMs include vehicle emission by applying Odd Even concept for all types of vehicles. 
# The vehicles with the odd last digit in the registration number will be allowed on roads on odd dates and those with even last digit will on even dates.

# Given an integer array a[], contains the last digit of the registration number of N vehicles traveling on date D(a positive integer). 
# The task is to calculate the total fine collected by the traffic police department from the vehicles violating the rules.

# Note : For violating the rule, vehicles would be fined as X Rs.

# Example 1:

# Input :

# 4 -> Value of N

# {5,2,3,7} -> a[], Elements a[0] to a[N-1], during input each element is separated by a new line

# 12 -> Value of D, i.e. date 

# 200 -> Value of x i.e. fine

# Output :

# 600  -> total fine collected 

# Explanation:

# Date D=12 means , only an even number of vehicles are allowed. 

# Find will be collected from 5,3 and 7 with an amount of 200 each.

# Hence, the output = 600.




def calculateFine(N, D, X):
    arr = []
    for i in range(N):
        v = int(input("enter day value:").strip())
        arr.append(v)
    count = 0
    if D % 2 == 0:
        for i in range(N):
            if arr[i] % 2 != 0:
                count += 1
    else:
        for i in range(N):
            if arr[i] % 2 == 0:
                count += 1
    return count*X 

N = int(input("Enter total days:").strip())
D = int(input("Enter value of Date:").strip())
X = int(input("Enter value of fine:").strip())

print(calculateFine(N, D, X))