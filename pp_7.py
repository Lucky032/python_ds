# rows = int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for space in range(1,rows-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()



# for i in range(rows-1, 0, -1):
#     for space in range(1, rows - i + 1):
#         print(" ", end="")
#     for j in range(1, 2 * i):  # Corrected star count
#         print("*", end="")
#     print()

rows = 6

num = 1
for i in range(rows):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()
        