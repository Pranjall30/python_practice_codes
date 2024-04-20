

def left_shift_string(s, shift):
    shift %= len(s)
    
    shifted_string = s[shift:] + s[:shift]
    return shifted_string

original_string = "hello"
shift_amount = 1
shifted_string = left_shift_string(original_string, shift_amount)
print("Shifted string:", shifted_string)
