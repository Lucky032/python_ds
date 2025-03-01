rows = int(input("Enter the number of rows: "))  # Define the number of rows

for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):  # Corrected space calculation
        print(" ", end="")

    for j in range(1, i + 1):
        print("* ", end="")  # Added space after the star

    print()  # Newline after each row