# arr = [4, 2, 1, 7, 8]
# k = 2
# max_sum = 0

# for i in range(len(arr) - k + 1):  # Iterate over all possible subarrays of size k
#     sub_array = arr[i:i+k]  # Extract the subarray of size k
#     sub_array_sum = sum(sub_array)  # Calculate its sum
#     max_sum = max(max_sum, sub_array_sum)  # Update max_sum if we find a larger sum

# print(max_sum)  # Output: 15 (from subarray [7, 8])


"""
Sliding window Algorithm
"""
arr = [4,2,1,7,8]
k = 2
max_sum = 0
for i in range(len(arr)-k+1):
    sub_array = arr[i:i+k]  # Extract the subarray of size k
    sub_array_sum = sum(sub_array)
    if sub_array_sum>max_sum:
        sub_array_sum = max_sum
    else:
        max_sum = max_sum
    print(max_sum)

        

    

