def add_person(people):
    # get details for person
    # make sure not to use the same dictionary
    # and overwrite it for details
    new_person_detail = {'Name': '','Age':'','Profession':'', 'Location':''}

    for key in new_person_detail.keys():
        new_person_detail[key] = input(f"Enter value for {key}: ")
    
    # if the dictionary is empty have to start numbering
    # choosing to do a sort of auto-increment on people
    # the value for the big dict is another dict
    max_key = 0
    if not len(people) == 0:
        max_key = max(people.keys())
        people[max_key+1] = new_person_detail

    else:
        people[0] = new_person_detail

# requires knowledge of person id
# and the people dictionary
def get_person(person_id, people):
    details = people[person_id]

    # once you extract the person
    # iterate over his details
    for detail in details:
        print(detail + ": " + details[detail])

# update a person by id
def update_person(person_id, people):
    person_details = people[person_id]

    for detail in person_details:
        person_details[detail] = input(f'Confirm or enter a new detail for person number  {person_id} detail {detail}: ')

# create a dictionary of people
people = {}

# add a couple of people to it
add_person(people)
add_person(people)

# retive a person by id in a certain dict
# output in function
get_person(0,people)
get_person(1,people)

# update person by id and dictionary
update_person(1,people)

for i in range(len(people)):
    get_person(i, people)






