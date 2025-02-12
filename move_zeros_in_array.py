# #move zeros 
# #given an integer array nums,move all 0's to the end of it while maintaining the relative order of the non-zero elements
# # input : nums = [0,1,0,3,12]
# #output = [1,3,12,0,0]

# non_zero_elements = 0
# nums = [0, 1, 0, 3, 12]

# for i in range(len(nums)):
#     print(i)
#     if nums[i] != 0:
#         nums[non_zero_elements] = nums[i]
#         non_zero_elements += 1

# for i in range(non_zero_elements, len(nums)):
#     nums[i] = 0

# print(nums)



    

zero_elements = 0
nums = [2,0,0,5,4]

for i in range(len(nums)):
    print(i)
    if nums[i] != 0:
     nums[zero_elements] = nums[i]
     zero_elements+=1

for i in range(zero_elements,len(nums)):
   nums[i] = 0
   print(i)