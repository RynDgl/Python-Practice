import csv

"""
practice writing to csv files.
"""
with open('test_write.csv', 'a') as csvfile:
    fieldnames = ['first_name', 'last_name', 'topic']
    teachwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    teachwriter.writeheader()
    teachwriter.writerow({
        'first_name': 'Ryan',
        'last_name': 'Daigle',
        'topic': 'Python |'
        })
        
