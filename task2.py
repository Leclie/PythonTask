import argparse
import logging

logging.basicConfig(filename='animal.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Animal:
    def __init__(self, name):
        self.name = name
        logger.info(f"Created Animal object with name: {self.name}")

    def __str__(self):
        return f"Name: {self.name}"

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
        logger.info(f"Created Bird object with name: {self.name} and wingspan: {self.wingspan}")

    def wing_length(self):
        logger.info(f"Calculating wing length for Bird object with name: {self.name}")
        return 100.0

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth
        logger.info(f"Created Fish object with name: {self.name} and max depth: {self.max_depth}")

    def depth(self):
        logger.info(f"Calculating depth for Fish object with name: {self.name}")
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        logger.info(f"Created Mammal object with name: {self.name} and weight: {self.weight}")

    def category(self):
        logger.info(f"Calculating category for Mammal object with name: {self.name}")
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create an animal object.')
    parser.add_argument('animal_type', type=str, choices=['Bird', 'Fish', 'Mammal'], help='Type of the animal')
    parser.add_argument('name', type=str, help='Name of the animal')
    parser.add_argument('--wingspan', type=float, help='Wingspan of the bird')
    parser.add_argument('--max_depth', type=int, help='Max depth of the fish')
    parser.add_argument('--weight', type=float, help='Weight of the mammal')
    return parser.parse_args()

def main():
    args = parse_arguments()
    animal_type = args.animal_type
    name = args.name

    animal = None
    if animal_type == 'Bird':
        wingspan = args.wingspan
        animal = AnimalFactory.create_animal(animal_type, name, wingspan)
        print(animal.wing_length())
    elif animal_type == 'Fish':
        max_depth = args.max_depth
        animal = AnimalFactory.create_animal(animal_type, name, max_depth)
        print(animal.depth())
    elif animal_type == 'Mammal':
        weight = args.weight
        animal = AnimalFactory.create_animal(animal_type, name, weight)
        print(animal.category())

    logger.info(f"Created {animal_type} object: {animal}")

if __name__ == '__main__':
    main()
