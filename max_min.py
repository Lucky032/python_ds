"""
Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9


Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
              Maximum element is: 35
"""
# arr = [3, 5, 4, 1, 9]
# grater = 0
# for i in arr:
#     if i>grater:
#         grater = i
# print("the greater number is ",grater)

arr = [3, 5, 4, 1, 9]
smallest = float('inf')
for i in arr:
    if i<smallest:
        smallest = i
print("the smallest number is: ",smallest)

