#sum odd minus even

l=[1,2,3,4,5]

sum_odd=0
sum_even=0

for x in l[0::2]:
     sum_odd+=x
for x in l[1::2]:
     sum_even+=x
print(sum_odd-sum_even)