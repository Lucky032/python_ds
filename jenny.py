# rows = int(input("Enter the number of rows: "))
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print("")
# for i in range(rows-1,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")

for i in range(1,27):
    for j in range(i):
        print(chr(65+j),end="")
    print()
