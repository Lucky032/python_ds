# nums_1 = [1,2,3,0,0,0]
# nums_2 = [2,5,6] 
# m = 3
# n = 3
# p1 = m-1
# p2 = n-1
# p = (m+n)-1

# while p1>=0 and p2>=0:
#     if nums_1[p1]>nums_2[p2]:
#         nums_1[p] = nums_1[p1]
#         p1 = p1-1
#     else:
#         nums_1[p] = nums_2[p2]
#         p2 = p2-1
# p = p-1


# while p2 >=0:
#     nums_1[p] = nums_2[p2]
#     p = p-1
#     p2 = p2-1

# print("Sorted Array:", nums_1)




nums_1 = [1, 2, 3, 0, 0, 0]
nums_2 = [2, 5, 6]
m = 3
n = 3
p1 = m - 1
p2 = n - 1
p = (m + n) - 1

# Shift non-zero elements to the left in nums_1
# for i in range(m, m + n):
#     nums_1[i] = 0

while p1 >= 0 and p2 >= 0:
    if nums_1[p1] > nums_2[p2]:
        nums_1[p] = nums_1[p1]
        p1 = p1 - 1
    else:
        nums_1[p] = nums_2[p2]
        p2 = p2 - 1
    p = p - 1

while p2 >= 0:
    nums_1[p] = nums_2[p2]
    p = p - 1
    p2 = p2 - 1

print("Sorted Array:", nums_1)
