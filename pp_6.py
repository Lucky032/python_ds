# # rows = int(input("Enter the number of rows: "))
# # for i in range(1,rows+1):
# #     for space in range(1,rows-i+1):
# #         print(" ")
# #         for j in range(1,2*i-1):
# #             print("*")
# #     print()

# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     # Print spaces
#     print(" " * i, end="")

#     # Print stars
#     print("*" * (2 * (rows - i) - 1))

#print solid rectangle
# for i in range(1,4):
#     for j in range(1,6):
#         print("*",end="")
#     print()

#Right-Angled Triangle (Left-Aligned):
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# Right-Angled Triangle (Right-Aligned):
# rows = int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for space in range(1,rows-i+1):
#         print(" ", end="")
#     for j in range(1, i+1):
#             print("*", end="")
#     print()

#Inverted Right-Angled Triangle (Left-Aligned):
# rows = int(input("Enter the number of rows: "))
# for i in range(rows, 0, -1):  # Corrected outer loop
#     for j in range(i):  # Corrected inner loop
#         print("*", end="")
#     print()

#Inverted Right-Angled Triangle (Right-Aligned):
# rows = int(input("Enter the number of rwos: "))
# for i in range(rows,0,-1):  # Hardcoded 5 rows
#     for space in range(rows-i):
#      print(" ",end="")
#     for j in range(i):
#         print("*", end="")
#     print()   

# rows = int(input("enter the number: "))
# for i in range(1,rows+1):
#     for space in range(1,rows-i+1):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()

# rows = int(input("enter the number: "))
# for i in range(rows,0,-1):
#     for space in range(rows-i):
#         print("*",end="")
#     for j in range(i):
#         print(" ",end="")
#     print()

# rows= int(input("Enter the number: "))
# for i in range(1,rows+1):
#     for space in range(1,rows-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()

# rows = int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for space in range(1,rows-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()


#Number Triangle (Increasing):
# rows = int(input("Enter the number of rows you need: "))
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")

#Number Triangle (Repeated):
# rows = int(input("Enter the number of rows you need: "))
# for i in range(1,rows+1):
#     for j in range(i):
#         print(i,end="")
#     print("")

# rows = int(input("Enter the number of rows you need: "))
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")

# rows = int(input("Enter the number of rows: "))
# count= 1
# for i in range(1,rows+1):
#     for j in range(i):
#         print(count ,end="")
#         count = count+1
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()


#zoho recently asked question
"""
1
2 4
3 5 7
6 8 10 12
9 11 13 15 17
14 16 18 20 22 24
"""

n = 6
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



for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
