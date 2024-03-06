import os
import string
def to_generate():
    for l in string.ascii_uppercase:
        filename = f"{l}.txt" 
        with open(filename, 'w') as file:
            file.write("some words and string")

to_generate()
