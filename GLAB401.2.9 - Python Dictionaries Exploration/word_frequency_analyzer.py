# determines word frequencies in user input.
# type 'quit' to exit program
freq = {}
line = input()
while line != 'quit':
  words = line.split()
  for word in words:
    freq[word] = freq.get(word, 0) + 1
  line = input()

# when 'quit' detected:
for word in freq:
  print(word), ': ', freq[word]
