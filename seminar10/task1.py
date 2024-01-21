class Animal:
    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    def __init__(self, name: str, wingspan: int):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan


class Fish(Animal):
    def __init__(self, name: str, max_depth: int):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth < 101:
            return 'Средневодная рыба'
        return 'Глубоководная рыба'


class Mammal(Animal):
    def __init__(self, name: str, weight: int):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight < 201:
            return 'Обычный'
        return 'Гигант'


class AnimalFactory:
    def create_animal(animal_type: str, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')


if __name__ == '__main__':
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

    print(animal1.wing_length())
    print(animal2.depth())
    print(animal3.category())
