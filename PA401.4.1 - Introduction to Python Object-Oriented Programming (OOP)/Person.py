# Task 1
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
        print("Person object created")

    # Task 3
    def display_info(self):
        print(f"Person Name: {self.name}, Person Age: {self.age}")
        
# Task 2
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

        print("Student object created")
        

# testing
if __name__ == "__main__":
    # task 1
    person = Person('Tav',2)

    # task 2
    student = Student('Spicoli', 17, 666)


    