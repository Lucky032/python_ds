count = 0
k = 3
current_sum = 0
arr = [1,2,3]
for i in range(len(arr)):   
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum == k:
            count += 1

print(count)

    

