answer = ['ring','the one ring','precious','the precious']

guess = input('What have I got in my pocket? ')

if guess.lower() in answer:
    print("Well I guess I get eaten, then.")
else: 
    print("It's something you just lost.")