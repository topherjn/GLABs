# determines word frequencies in user input.
# type 'quit' to exit program
freq = {}
text = 'Four score and seven years ago our fathers \
brought forth, upon this continent, a new nation, \
conceived in liberty, and dedicated to theproposition \
that all men are created equal. Now we are engaged in \
a great civil war, testing whether that nation, or \
any nation so conceived, and so dedicated, can long \
endure. We are met on a great battle field of that \
war. We come to dedicate a portion of it, as a final \
resting place for those who died here, that the nation \
might live. This we may, in all propriety do.'

text = text.lower()

letters = ('a','b','c','d','e','f','g','h','i','j','k'
           ,'l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z',' ')

filtered_words = ''
for character in text:
   if character in letters:
      filtered_words += character

print(filtered_words)

words = filtered_words.split()

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word in freq:
  print(word, ': ', freq[word])
