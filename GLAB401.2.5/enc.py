#!/usr/bin/python
from sys import argv

# Define the key here:
key = {'a':'q','b':'g','c':'d','d':'e','e':'p','f':'r','g':'t','h':'y','i':'k','j':'u','k':'i','l':'o','m':'j','n':'h','o':'l','p':'z','q':'a','r':'f','s':'w','t':'v','u':'m','v':'x','w':'s','x':'b','y':'n','z':'c'}

#main
if len(argv) != 2:
  print('Usage: >> ./enc.py input_file')
  exit()

fr = open(argv[1])
fw = open("encrypted_"+argv[1], "w")

file_content = fr.read()
fr.close()
file_content = file_content.lower()
content = list(file_content)
i = 0
while i<len(content):
  if content[i] in key:
    content[i] = key[content[i]]
  i+=1

output = "".join(content)
fw.writelines(output)

fw.close()