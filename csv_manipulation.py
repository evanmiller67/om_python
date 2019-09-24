#/usr/bin/env python3
"""
title: csv_manipulation.py
author: exm5840
date(created): 2019-09-19 16:43:08 EDT
date (updated): 2019-09-19 16:43:08 EDT
"""
import csv


#with open('addresses.csv','r') as address_data:
#    read_address_data = csv.reader(address_data)
#    list_address_data = list(read_address_data)     ## We now have a table of data
#
#for i, row in enumerate(list_address_data):
#    print(f"Row #: {i} {row}")
#
#
### These lists are mutable
#list_address_data[2] = ['Reese', 'Witherspoon', '362 Main St', 'Austin', 'TX', '78704']
#list_address_data[3][0] = 'Elizabeth'
#
#
#with open('addresses.csv', 'w') as address_data_file:
#    write_address_data = csv.writer(address_data_file)
#    write_address_data.writerows(list_address_data)
#    write_address_data.writerow(['Alegra', 'Cole', '1 Broadway Rd', 'New York City', 'NY', 15432])


## Use an _ordered_ dictionary
with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)
    headers = reader.fieldnames
    addresses = list(reader)        ## Printing this is an array of dictionaries
    for row in reader:
        print(row['Last Name'])

## Remove the 'Address Line' from every row
for row in addresses:
    del row["Address Line"]
headers.remove('Address Line')      ## Make sure to do this to avoid Nulls when writing the file


with open('addresses_altered.csv', 'w') as address_data:
    writer = csv.DictWriter(address_data, fieldnames=headers)
    writer.writeheader()
    writer.writerows(addresses)
