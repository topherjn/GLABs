class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def print_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

        

# testing
if __name__ == "__main__":
    person = Person('Tav',2)
    person.print_person()
    