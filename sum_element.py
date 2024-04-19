#SUM of elements in a list

elements = input("Enter the list elements separated by space: ")

element_list = list(map(int, elements.split()))

sum_of_elements = sum(element_list)

print("The sum of the elements in the list is: ", sum_of_elements)
