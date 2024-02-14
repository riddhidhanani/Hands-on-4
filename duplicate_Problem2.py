array = [1,2,2,3,3,4,4,4,5,5]
no_dupli = set()
count = 0
for i in range(len(array)):
    i = i-count
    if array[i] in no_dupli:
         array.remove(array[i])
         count+=1
    else:
         no_dupli.add(array[i])

print(array)

# OUTPUT
# [1, 2, 3, 4, 5]

# TIME COMPLEXITY

# 1. Loop:O(N) - The for loop iterates through each element in the array once.
# 
# 2. Set Operations: O(1) average, O(N) worst-case - The in and add operations on the set no_dupli are generally constant time on average but could be linear in the worst case.
# 
# 3. List Removal: O(N) - The remove operation on the list can take up to linear time in the worst case since it may need to shift elements after the removal point.
# 
# Overall, the worst-case time complexity is determined by the list removal operation inside the loop. As a result, the overall time complexity is O(N^2), where N is the length of the array.
