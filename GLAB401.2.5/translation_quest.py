"""
The Quest for Translation: Create a program that acts as a translator. Use a dictionary to store words and their translations. Prompt the user to enter a word and display its translation if it exists in the dictionary.
"""
translation_dictionary = {}
translation_dictionary['apple'] = 'pomme'
translation_dictionary['man'] = 'homme'
translation_dictionary['woman'] = 'femme'
translation_dictionary['red'] = 'rouge'
translation_dictionary['sky'] = 'ciel'
translation_dictionary['earth'] = 'terre'
translation_dictionary['keyboard'] = 'clavier'
translation_dictionary['tooth'] = 'dent'
translation_dictionary['water'] = 'eau'
translation_dictionary['eye'] = 'oeil'


word = input("Enter an English word to translate into French: ")

if word in translation_dictionary: 
    print(f"{word} is {translation_dictionary[word]} in French")
else:
    print("Word is not in dictionary")
