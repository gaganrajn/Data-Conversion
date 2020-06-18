import csv 
import pprint 
from timeit import default_timer as timer 

read_file = input("Enter the file path: ")
start = timer() 
with open(read_file) as csvfile: 
    reader = csv. DictReader(csvfile)
    field = reader.fieldnames
    csv_rows = [] 
    for row in reader: 
        csv_rows.append({field[i]:row[field[i]] for i in range(len(field))})
                          
for i in csv_rows:
    pprint. pprint(i)
end = timer()    
print("The time taken to convert from CSV to JSON format is :", str(end-start)+"s")