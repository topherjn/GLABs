# Create a new Python file named "word_wrangler.py."
    # Done
# Define a sentence variable with a meaningful sentence.
sentence = 'Inoffensive speech needs no protection.'
# Use string methods to count the number of words in the sentence.
words = sentence.split()
print(len(words))
# Identify and print the longest word in the sentence.
biggest_word = words[0]
max = len(biggest_word)

for word in words[1:]:
    if len(word) > max:
        biggest_word = word
        max = len(word)
print("Longest word: " + biggest_word)

# Capitalize the first letter of each word in the sentence.
sentence = words[0]
for word in words[1:]:
    sentence += ' ' + word[0].upper() + word[1:]

print(sentence)
