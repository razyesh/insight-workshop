"""
Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22

John,54 Love Ave,21
"""
import csv


def generate_csv(filename, user_info):
    """
    function to generate CSV file
    :param filename: filename to write our data
    :param user_info: data to write into csv file
    :return: returns nothing but generate csv file
    """
    fieldname = ('name', 'address', 'age')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldname)

        writer.writerows(user_info)


if __name__ == "__main__":
    filename = 'demo.csv'
    sample_input = [('ram','kapann', 23), ('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
    generate_csv(filename, sample_input)