# calculate interaction of two arrays

def array_intersection(array1, array2):
    return list(set(array1) & set(array2))

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
print(array_intersection(array1, array2))