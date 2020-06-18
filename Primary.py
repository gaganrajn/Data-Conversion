import csv
import pprint
from timeit import default_timer as timer 


read_file='D:\chrome\c.csv'

start = timer()
with open(read_file) as csvfile:
    reader = csv.DictReader(csvfile)
    field = reader.fieldnames
    csv_rows = []
    for row in reader:
        csv_rows.append(({field[i]:row[field[i]]  for i in range(len(field))}))
        
for i in csv_rows:
    
        pprint.pprint(i)
        
end = timer()
print("The time taken to convert from .csv to .json format is:", end - start) 





