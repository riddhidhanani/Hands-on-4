k = 3
N = 4
array1 = [1,3,5,7]
array2 = [2,4,6,8]
array3 = [0,9,10,11]
sorted_array=[]

array1.extend(array2)
array1.extend(array3)

array1.sort()
print(array1)

# OUTPUT
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# To analyze the time complexity of the given algorithm,
# 
# 1. Merging Arrays: The `extend` operation is used to concatenate `array2` and `array3` to `array1`. Since this operation depends on the length of the arrays, it takes O(N) time, where N is the total number of elements across all arrays.
# 
# 2. Sorting: The `sort` operation is applied to the merged array `array1`. The time complexity of the sorting operation is O(N \log N) for the average case. 
# 
# 3. Printing: The `print` statement doesn't affect the overall time complexity, as it's considered a constant-time operation.
# 
# Therefore, the dominant factor contributing to the time complexity is the sorting operation, which is O(N \log N).
# 
# In conclusion, the time complexity of this algorithm is O(N \log N)