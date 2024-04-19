#Take N number as input and print their sum

n = int(input("Enter n: "))
sum = 0

for i in range(n):
    num = int(input("Enter numbers {i+1}: "))
    sum += num

print("The sum of numbers is: " ,sum)