import csv
import utils_csv as us
#with open('test.csv', 'rb')as csvfile:
#    reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
#    for row in reader:
#        print ','.join(row)

print us.create_file( us.categorize_items(us.read_csv('test.csv', 'rb', ' '), 0))
