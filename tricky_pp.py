# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# n = 6
# odd = 1
# even = 2

# for i in range(1, n + 1):
#     for j in range(i): # ekada i petanu kada adi i times repet itadhi ante i = 3 ante 0,1,2' so ee 3 values consider cheskuntadhi
#         if i % 2 == 1:  # Odd rows contain odd numbers
#             print(odd, end=" ")
#             odd += 2
#         else:  # Even rows contain even numbers
#             print(even, end=" ")
#             even += 2
#     print()

# n = 6
# odd = 1
# even = 2

# for i in range(1, n + 1):
#     for j in range(i):  # i times repetition
#         if i % 2 == 1:  # Odd rows contain odd numbers
#             print(odd, end=" ")
#             odd += 2
#         else:  # Even rows contain even numbers
#             print(even, end=" ")
#             even += 2
#     print()





# nums = [2,2,1,1,1,2,2]
# n = sum(nums) / len(nums)
# count = 0
# repet = 0
# for i in nums:
#     if i>n:
#      repet=i
#     else:
#        break
# print(repet)

# nums = [2,2,1,1,1,2,2]
# print(len(nums))

# rows = 6
# start_values = [1, 7, 12, 16, 19, 21]

# for i in range(rows):
#     current_value = start_values[i]
#     for j in range(i + 1):
#         print(current_value, end=" ")
#         if i - j > 0:
#             current_value -= (rows - i + j)
#         else:
#             current_value += (rows - i - j)
#     print()


n = 6
odd = 1
even = 2

for i in range(1, n + 1):
    for j in range(i):  # i times repetition
        if i % 2 == 1:  # Odd rows contain odd numbers
            print(odd, end=" ")
            odd += 2
        else:  # Even rows contain even numbers
            print(even, end=" ")
            even += 2
    print()


    