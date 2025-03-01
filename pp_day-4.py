rows = int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for space in range(1,rows-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()

# rows = int(input("Enter the number of rows: "))
# for i in range(1, rows + 1):
#     for space in range(1, rows - i + 1):
#         print(" ", end="")
#     for j in range(1, 2 * i):  
#         print("*", end="")
#     print()


# rows = int(input("Enter the number of rows: "))

# for i in range(rows, 0, -1):  # Reversed outer loop
#     # Print leading spaces (for centering)
#     for space in range(1, rows - i + 1):
#         print(" ", end="")

#     # Print stars (2*i - 1 for the correct number of stars)
#     for j in range(1, 2 * i):
#         print("*", end="")

#     print()  # Newline after each row