#Given a number, calculate it's nearest power of two

n = int(input("Enter a number:"))
p = 1
while p < n:
    p<<=1
print("The nearest power of two for", n, "is:" ,p)