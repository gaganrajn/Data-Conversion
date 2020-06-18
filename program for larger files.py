import json
import csv
from timeit import default_timer as timer 
start = timer()
f = open('D:\chrome\c.csv', 'r')
reader = csv.DictReader(f)

jsonoutput = 'D:\chrome\myfile.json'
with open(jsonoutput, 'a') as f:
    for i in reader:
       
        json.dump(i ,f,sort_keys=False, indent=4, separators=(',', ': '))
        
        f.write('\n')
end = timer()        
print("The time taken to convert from .csv to .json format is:", end - start) 
