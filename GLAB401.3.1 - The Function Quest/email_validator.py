def email_validator(email_address):
    # the approach I am taking is to assume the email is valid
    # and return True by default, but to put a series 
    # of False hurdles in the way of that

    # without googling, I think this filter contains the only allowed 
    # characters.  Reject those right away from the top
    allowed_characters = ("+","-","_","@",".","a","b","c","d","e","f","g","h",
                          "i","j","k","l","m","n","o","p","q","r","s",
                          "t","u","v","w","x","y","z","1","2","3","4",
                          "5","6","7","8","9","0")
    for character in email_address:
        if character not in allowed_characters:
            return False
        
    # email must have precisely one @
    if email_address.count('@') != 1:
        return False
    # has to be at least one .    
    if '.' not in email_address:
        return False
    # some things can't be at the beginning
    if email_address[0] in ("+","@",".","-","_","1","2",
                            "3","4","5","6","7","8","9","0"):
       return False 
    
    # some things can't be at the end
    if email_address[len(email_address)-1] in ("+","@",".",
                                               "-","_","1","2",
                                                "3","4","5","6",
                                                "7","8","9","0"):
        return False
    
    # also must have space between them
    if '@.' in email_address or '..' in email_address:
        return False
    
    # can't have more than one at
    if email_address.count('@') > 1:
        return False
    
    return True

# testing.  I think more sophistication beyond this will require regex
print('nicholson@gmail.com is', ' not ' if not email_validator('nicholson@gmail.com') else ' ', 'a valid email address.', sep='')

print('nicholson@@gmail.com is', 'not' if not email_validator('nicholson@@gmail.com') else ' ', 'a valid email address.')

print('nicholson@gmail.com@ is', 'not' if not email_validator('nicholson@gmail.com@') else ' ', 'a valid email address.')

print('nicholson@gmail..com is', 'not' if not email_validator('nicholson@gmail..com') else '', 'a valid email address.')

print('nichol?son@gmail.com is', 'not' if not email_validator('nichol?son@gmail..com') else ' ', 'a valid email address.')