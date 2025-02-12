# arr = [1,2,3,4]
# start = 0
# end = len(arr)-1

# while (start<end):
#     temp = arr[start]
#     arr[start] = arr[end]
#     arr[end] = temp
#     start = start+1
#     end = end-1
# print(arr)
# s = arr[::-1]



"""
Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5.
 After reversing the array, the first element goes to the 
 last position, the second element goes to the second last 
 position and so on. Hence, the answer is 5 6 2 3 4 1.
"""



def solveMeFirst(a,b):
    return a+b
	# Hint: Type return a+b below


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)


print(res)