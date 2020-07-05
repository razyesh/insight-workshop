"""
14. Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
"""
import csv


def csv_file_reader(filename):
    """
    function that reads csv file
    :param filename: name of the file which to be read
    :return: list containing detail about user in dict format
    """
    dict_output = {}
    result = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_output['name'] = row['name']
            dict_output['address'] = row['address']
            dict_output['age'] = row['age']
            result.append(dict_output)
            dict_output = {}

    return result


if __name__ == "__main__":
    filename = 'demo.csv'
    result = csv_file_reader(filename)
    print(result)
