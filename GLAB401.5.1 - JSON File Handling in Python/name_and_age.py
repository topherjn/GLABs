import json

# task 4
# open the file for reading
try:
    with open("my_file.json",'r') as my_file_fp:
        my_file_data = json.load(my_file_fp)
except Exception as ex:
    print(ex)
# go through each person printing out details
for person in my_file_data:
    print(f"Name: {person['name']}, Age: {person['age']}")