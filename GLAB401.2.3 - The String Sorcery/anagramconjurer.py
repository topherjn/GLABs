"""
The Anagram Conjurer: Write a program that prompts the user to 
enter two words or phrases. Determine if they are anagrams 
(contain the same characters in different orders) and reveal 
the secret connection between them.
"""

#nb doesn''t doesnt filter spaces or punctuation

# get each individual letter into a list, retaining duplicates
# sort both lists the same way
phrase1 = list(input("Enter the first phrase: ").lower())
phrase2 = list(input("Enter the second phrase: ").lower())

phrase1.sort()
phrase2.sort()

# if the lists are the same you have anagrams
# print the sorted list
if phrase1 == phrase2:
    print("The two phrases are anagrams.")
    print(''.join(phrase1))

else:
    print("The two phrases are not anagrams.")