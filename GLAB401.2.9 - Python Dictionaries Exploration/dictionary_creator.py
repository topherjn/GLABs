# create dictionary of pet nicknames and "real names"
pet_names = { 'Crispy' : 'Charles Crispen Peabody', 
              'Brownie' : 'Elizabeth Barrett Brownie',
              'Granny-Baby' : 'Vegas',
              'Mommadawg' : 'Sugary',
              'Shelly' : 'Shelton Allen'}

# update a key
pet_names['Shelley'] = pet_names['Shelly']
print('Deleting old key for ' + pet_names.pop('Shelly'))

# add pets
pet_names['Peeps'] = 'Penelope'
pet_names['Dummy'] = "Non-existant pet I won't feel bad about deleting"
pet_names['Fake'] = "Non-existant pet I won't feel bad about deleting"

# remove a pet
print("Deleting " + pet_names.pop('Dummy'))
del pet_names['Fake']

# update a value
pet_names['Crispy'] = 'Charles Crispin Peabody'

# list final contents of dictionary
print("\nFinal contents of dictionary: ")
for pet in pet_names:
    print(f'Nickname: {pet}, "Real" name: {pet_names[pet]}')

