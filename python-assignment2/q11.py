"""
Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?
"""
import os


def get_filename():
    """Function to get the name of file without extension"""
    file_names = []
    for i in os.listdir():
        if '.' in i:
            file_names.append(i.split('.')[0])

    return file_names


result = get_filename()
print(result)

