class Human:

    MAX_ENERGY = 100

    def __init__(self, name='Human', age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY
