class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, intelligence_level):
        super().__init__(name, age, coat_color)
        self.intelligence_level = intelligence_level

    def bark(self):
        print(f"{self.name} is barking loudly!")

    def jump(self):
        print(f"{self.name} is jumping around!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def snore(self):
        print(f"{self.name} is snoring loudly!")

    def tug_of_war(self):
        print(f"{self.name} is playing tug of war!")


# Create objects and implement the functionalities
dog1 = Dog("Max", 5, "Brown")
dog1.description()
dog1.get_info()

terrier = JackRussellTerrier("Rocky", 3, "White and Brown", "High")
terrier.description()
terrier.get_info()
terrier.bark()
terrier.jump()

bulldog1 = Bulldog("Spike", 4, "White", "Strong")
bulldog1.description()
bulldog1.get_info()
bulldog1.snore()
bulldog1.tug_of_war()