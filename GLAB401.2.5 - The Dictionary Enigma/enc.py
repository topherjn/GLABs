"""The Cryptic Encoder: Write a program that encrypts a message using a simple substitution cipher. Use a dictionary to map each letter to its corresponding encrypted value. Decrypt the message using the reverse mapping."""

# sister file: dec.py

#!/usr/bin/python
from sys import argv

# Define the key here:
key = {'a':'q','b':'g','c':'d','d':'e','e':'p','f':'r','g':'t','h':'y','i':'k','j':'u','k':'i','l':'o','m':'j','n':'h','o':'l','p':'z','q':'a','r':'f','s':'w','t':'v','u':'m','v':'x','w':'s','x':'b','y':'n','z':'c'}

#main
if len(argv) != 2:
  print('Usage: >> ./enc.py input_file')
  exit()

# open the file specified on command line for reading
# open a new file to save translation
# name of translation file built from read file
fr = open(argv[1])
fw = open("encrypted_"+argv[1], "w")

# read all the contents into one string
file_content = fr.read()
fr.close()

# make all content lower case
file_content = file_content.lower()

# turn the letters into a list
content = list(file_content)

# turn letters into substitute letters
i = 0
while i<len(content):
  if content[i] in key:
    content[i] = key[content[i]]
  i+=1

# turn list into string and write to file
output = "".join(content)
fw.writelines(output)

fw.close()