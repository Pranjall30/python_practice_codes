#Write a function to print distinct element from an array

def print_distinct_elements(array):
    print(set(array))

array = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print_distinct_elements(array)