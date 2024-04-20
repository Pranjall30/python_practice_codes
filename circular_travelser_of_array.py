

def circular_traversal(array, direction, steps):
    length = len(array)
    index = 0
    if direction == "right":
        index = (index + steps) % length
    elif direction == "left":
        index = (index - steps) % length
    else:
        raise ValueError("Invalid direction. Must be 'right' or 'left'.")
    return array[index]

array = [1, 2, 3, 4, 5]
print(circular_traversal(array, "right", 2))
print(circular_traversal(array, "left", 2))