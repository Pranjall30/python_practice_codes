# Print a hollow rectangle with asterisks

rows = int(input("Enter the number of Rows  : "))
columns = int(input("Enter the Number of Columns  : "))

for i in range(rows):
    for j in range(columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end ="")
        else:
            print(' ', end = "")
    print()