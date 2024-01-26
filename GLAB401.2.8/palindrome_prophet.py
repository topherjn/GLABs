# Create a new Python file named "palindrome_prophet.py."
    # done
# Define a function that checks if a given string is a palindrome.
alphanumeric = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0")
def is_palidrome(phrase):
    phrase = phrase.lower()
    filtered_phrase = ''
    # Handle edge cases"," such as ignoring spaces and punctuation.
    for letter in phrase:
        if letter in alphanumeric:
            filtered_phrase += letter
    
    phrase = filtered_phrase

    return phrase == phrase[::-1]
# Test the function with various strings"," including phrases and sentences.

phrase = input("Enter a phrase to test: ")

# Print the results.
print(is_palidrome(phrase))




