#Calculate sum of each column in 2D array

array = [[1,4,3,6],
        [ 4,7,9,8],
        [ 2,5,6,7],
        [ 5,7,8,9]]

col_sums = [sum(col) for col in array]
print(col_sums)