#Write a function to search a string in an array

def search_string(array, string):
    for row in array:
        if string in row:
            return True
    return False

array = [["AB", "CD", "EF"],
         ["JH", "IJ", "LM"],
         ["NO", "PQ", "RS"]]

string = "AJ"
print(search_string(array, string))