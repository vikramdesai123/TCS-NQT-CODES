# An international round table conference will be held in india. Presidents from all over the world representing their respective countries will be attending the conference. The task is to find the possible number of ways(P) to make the N members sit around the circular table such that.

# The president and prime minister of India will always sit next to each other.

# Example 1:

# Input :

# 4   -> Value of N(No. of members)

# Output : 

# 12  -> Possible ways of seating the members

# Explanation:

# 2  members should always be next to each other. 

# So, 2 members can be in 2!ways

# Rest of the members can be arranged in (4-1)! ways.(1 is subtracted because the previously selected two members will be considered as single members now).

# So total possible ways 4 members can be seated around the circular table 2*6= 12.

# Hence, output is 12.



# using recursion
def count_Ways_of_Seating(M):
    if M == 0 or M == 1:
        return 1 
    return M * count_Ways_of_Seating(M -1)

N = int(input("Enter total number of members:").strip())
M = N - 1 
print(count_Ways_of_Seating(M) * 2)