#sum adjacent values in an array

array = "1,2,3,4"
array_list = array.split(',')
sum = 0
for i in range(len(array_list)):
    if i < len(array_list) - 1:
        sum += int(array_list[i]) + int(array_list[i+1])
print(sum)
