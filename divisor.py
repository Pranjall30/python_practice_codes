#give a number and print its divisor

n = int(input("Enter n:"))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

