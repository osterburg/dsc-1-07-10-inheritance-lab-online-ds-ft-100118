class Animal(object):
    def __init__(self, name, weight):
        self.name = name
        self.size = None
        self.weight = weight
        self.species = None
        self.food_type = None
        self.nocturnal = False

    def sleep(self):
        if self.sleep:
            print("{} sleeps at day time".format(self.name))
        else:
            print("{} sleeps at night time".format(self.name))

    def eat(self, food):
        if self.food_type == 'omnivore':
            print("{} the {} thinks {} is Yummy!".format(self.name, self.species, food))
        elif (food == 'meat' and self.food_type == "carnivore") or \
                (food == 'plants' and self.food_type == 'herbivore'):
            print("{} the {} thinks {} is Yummy!".format(self.name, self.species, food))
        else:
            print('I do not eat this!')


class Elephant(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'elephant'
        self.size = 'enormous'
        self.food_type = 'herbivore'
        self.nocturnal = False


class Tiger(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'tiger'
        self.size = 'large'
        self.food_type = 'carnivore'
        self.nocturnal = True


class Raccoon(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'raccoon'
        self.size = 'small'
        self.food_type = 'omnivore'
        self.nocturnal = True


class Gorilla(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'gorilla'
        self.size = 'large'
        self.food_type = 'herbivore'
        self.nocturnal = False


def add_animal_to_zoo(zoo, animal_type, name, weight):
    if animal_type is "Gorilla":
        animal = Gorilla(name, weight)
    elif animal_type is "Raccoon":
        animal = Raccoon(name, weight)
    elif animal_type is "Tiger":
        animal = Tiger(name, weight)
    else:
        animal = Elephant(name, weight)

    return zoo.append(animal)


def feed_animals(zoo, time='Day'):
    for animal in zoo:
        if time == 'Day':
            if not animal.nocturnal:
                if animal.food_type is 'carnivore':
                    animal.eat('meat')
                else:
                    animal.eat('plants')
        else:
            if animal.nocturnal:
                if animal.food_type is 'carnivore':
                    animal.eat('meat')
                else:
                    animal.eat('plants')


zoo = []

add_animal_to_zoo(zoo, 'Elephant', "dumbo1", 200)
add_animal_to_zoo(zoo, 'Elephant', "dumbo1", 520)
add_animal_to_zoo(zoo, 'Raccoon', "raccoon1", 20)
add_animal_to_zoo(zoo, 'Raccoon', "raccoon2", 12)
add_animal_to_zoo(zoo, 'Gorilla', "gorilla", 120)
add_animal_to_zoo(zoo, "Tiger", "tiger1", 70)
add_animal_to_zoo(zoo, "Tiger", "tiger2", 80)
add_animal_to_zoo(zoo, "Tiger", "tiger3", 75)

feed_animals(zoo)
feed_animals(zoo, 'Night')
