#Print ordered pair which can be formed using first N numbers

n = int(input("Enter n:"))

for i in range (n+1):
    for j in range (n+1):
        print((i,j))
