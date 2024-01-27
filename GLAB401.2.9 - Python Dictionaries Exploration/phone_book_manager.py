def add_entry(name,phone_book):
    number = input(f"What is the phone number for {name}? ")
    numeral_filter = ('0','1','2','3','4','5','6','7','8','9')

    phone_number = ''
    for digit in number:
        if digit in numeral_filter:
            phone_number += digit
    if len(phone_number) == 10:        
        phone_book[name] = phone_number
    else:
        print("Invalid phone number")

def remove_entry(name, phone_book):
    print(f"Deleting entry for {name} " + phone_book.pop(name))

def print_entry(name, phone_book):
    print(f"{name}'s phone number is {phone_book[name]}")

# simple list for phone numbers
# name and entry
# not checking for duplicates
phone_book = {}

# add an entry
add_entry('Chris',phone_book)

# lookup entry
print_entry('Chris', phone_book)

# remove an entry
remove_entry('Chris',phone_book)


