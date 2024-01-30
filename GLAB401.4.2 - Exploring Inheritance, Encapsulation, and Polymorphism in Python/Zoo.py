class Animal:
    def __init__(self, name, species, age) -> None:
        self.name = name
        self.species = species
        self.age = age
    
    def make_sound(self):
        pass

class Mammal(Animal):
    def __init__(self, name, species, age, fur_color) -> None:
        super().__init__(name, species, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Roar")

class Bird(Animal):
    def __init__(self, name, species, age, feather_color) -> None:
        super().__init__(name, species, age)
        self.feather_color = feather_color
        
    def make_sound(self):
        print("Tweet")

class Zookeeper:
    def __init__(self, name):
        self.name = name
        self.__log = []

    def feed(self, animal, amount):
        entry =("feed", animal, amount)
        self.__log.append(entry)

    def clean(self, animal, how_dirty):
        entry = ("clean", animal, how_dirty)
        self.__log.append(entry)

    def observe(self, animal, behavior):
        entry = ("observe", animal, behavior)
        self.__log.append(entry)

    def print_log(self):
        for entry in self.__log:
            print(entry)



# testing
if __name__=="__main__":
    bird = Bird('Rocky','Rooster', 12, 'red')

    bird.make_sound()

    parrot = Bird('Polly', 'Parrot', 2, 'green')

    monkey = Mammal('Cloe','Spider', 5, 'brown')
    
    lion = Mammal('Leo', 'Lion', 'tawny', 4)

    # logging events
    zookeeper = Zookeeper("Joe")
    zookeeper.clean('Leo','very dirty')
    zookeeper.observe('Polly','Eating cracker')
    zookeeper.feed('Cloe','banana')
    zookeeper.observe('Cloe','spitting')

    # print out log
    zookeeper.print_log()
    






