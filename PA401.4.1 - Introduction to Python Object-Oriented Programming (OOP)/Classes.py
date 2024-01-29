# Task 1
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        self.__secret = 616
        
        print("Person object created")

    # Task 3
    def display_info(self):
        print(f"\nName: {self.name}, Age: {self.age}", end="")

    # Task 4
    def reveal_secret(self):
        print('Secret: ',self.__secret)

# Task 2
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

        print("Student object created")

    # Task 3
    def display_info(self):
        super().display_info()
        print(f", Student ID: {self.student_id}")



# testing
if __name__ == "__main__":
    # task 1
    person = Person('Tav',2)

    # task 2
    student = Student('Spicoli', 17, 666)

    # task 3
    print("\nDisplaying info: ")
    person.display_info()
    student.display_info()

    # task 4
    person.reveal_secret()

    # can't access the private variable directly
    try:
        print(person.__secret)
    except Exception: # should really to catch specific exception
        print("You can't touch the secret!")