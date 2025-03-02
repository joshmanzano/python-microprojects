# File handling
import csv
# https://docs.python.org/3/library/csv.html

with open('colorectal_cancer_dataset.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i, row in enumerate(reader):
        print(', '.join(row))
        if i == 5:  # Stop after printing 5 rows
            break