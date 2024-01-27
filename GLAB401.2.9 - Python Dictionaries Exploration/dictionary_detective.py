# create a dictionary for a generic person
person_info = {'name' : '', 
               'age': '', 
               'profession':'', 
               'location': ''}

def add_person(people):
    # get details for person
    new_person_detail = person_info.copy()
    for key in new_person_detail.keys():
        new_person_detail[key] = input(f"Enter value for {key}: ")
    
    if not len(people) == 0:
        max_key = max(people.keys())
        people[max_key+1] = new_person_detail

    people[0] = new_person_detail

def get_person(person_id, people):
    details = people[person_id]

    for detail in details:
        print(detail + ": " + details[detail])

# create a dictionary of people
people = {}

add_person(people)
add_person(people)

get_person(0,people)




