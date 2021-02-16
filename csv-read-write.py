# https://docs.python.org/3/library/csv.html
# https://realpython.com/python-csv/

import csv
from pathlib import Path

# Read CSV
# The csv has been exported by Excel as utf-8 with ';' as separator

with open('sample-data/books.csv', 'r', newline='', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tBook: {row[0]}, author: {row[1]}, rating: {row[2]}, year: {row[3]}.')
            line_count += 1
            
    print(f'Processed {line_count} lines.')
    print()


# csv.DictReader() example: access the row as dictionary with heading column names

with open('sample-data/books.csv', 'r', newline='', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tBook: {row["title"]}.')
            line_count += 1
            
    print(f'Processed {line_count} lines.')

# Write CSV

# create output dir
Path("output").mkdir(parents=True, exist_ok=True)

with open('output/employee_file.csv', mode='w', newline='', encoding='utf-8') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# Write CSV from a Dictionary

with open('output/employee_file2.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})