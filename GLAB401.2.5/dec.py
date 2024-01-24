#!/usr/bin/python
from sys import argv

# Define the key here:
key = {'a':'q','b':'g','c':'d','d':'e','e':'p','f':'r','g':'t','h':'y','i':'k','j':'u','k':'i','l':'o','m':'j','n':'h','o':'l','p':'z','q':'a','r':'f','s':'w','t':'v','u':'m','v':'x','w':'s','x':'b','y':'n','z':'c'}

# For Decryption, make sure to reverse the Encryption key:
key = dict(zip(key.values(), key.keys()))

# Check key to make sure there are no duplicate values:
list_key = key.values()
for item in list_key:
  if list_key.count(item) != 1:
     print("possible problem with: ", item, " count is: ", list_key.count(item))

#main
if len(argv) != 2:
  print('Usage: >> ./dec.py input_file')
  exit()

fr = open(argv[1])
fw = open("decrypted_"+argv[1], "w")

file_content = fr.read()
file_content = file_content.lower()
content = list(file_content)
i = 0
while i<len(content):
  if key.has_key(content[i]):
    content[i] = key[content[i]]
  i+=1

output = "".join(content)
fw.writelines(output)

fr.close()
fw.close()