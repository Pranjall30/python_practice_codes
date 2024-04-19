#Print first N terms of a GP with given first term, N and common ration

n = int(input("Enter n: "))
a = int(input("Enter the first term: "))
r = int(input("Enter the common ratio: "))

for i in range(n):
    print(a * (r**i), end=" ")