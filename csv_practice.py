
import csv

"""
Reading CSV
also check out tabreader library
"""

with open("test_write.csv", ) as csvfile:
    artreader = csv.DictReader(csvfile, delimiter='|')
    rows = list(artreader)
    for row in rows[:2]:
        print(row)
