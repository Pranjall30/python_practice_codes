#palindrome or not

str='131131'

if str[:] == str[:: -1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")