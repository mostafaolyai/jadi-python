class Zoo:
    zoo_name = "Zoo One"

    def __init__(self, animal):
        self.animal = animal

    def info(self):
        print(
            f"Name: {self.animal.name}\n"
            f"Species: {self.animal.species}\n"
            f"Age: {self.animal.age}\n"
            f"Sound: {self.animal.sound}"
        )


class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} is making sound: {self.sound}")

    def info(self):
        print(
            f"Name: {self.name}\n"
            f"Species: {self.species}\n"
            f"Age: {self.age}\n"
            f"Sound: {self.sound}"
        )


class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span


shir = Animal("Shir", "Darandeh", "12", "huaaaaa")
# shir.info()


zoo = Zoo(shir)
zoo.info()
