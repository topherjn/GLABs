# Create a new Python file named "palindrome_prophet.py."
    # done
# Define a function that checks if a given string is a palindrome.
def is_palidrome(phrase):
    phrase = phrase.lower()
    
    # Handle edge cases, such as ignoring spaces and punctuation.

    # researched how to add only alpha and numerals
    # https://nadeauinnovations.com/post/2020/11/python-tricks-replace-all-non-alphanumeric-characters-in-a-string/
    phrase = filter(lambda x: x.isalnum(), phrase)
    phrase = "".join(phrase)
    
    return phrase == phrase[::-1]
# Test the function with various strings, including phrases and sentences.

phrase = input("Enter a phrase to test: ")

# Print the results.
print(is_palidrome(phrase))




