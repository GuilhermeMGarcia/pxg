import random


class Pokemon:

    def __init__(self, especie, lvl=None, nome=None):
        self.especie = especie
        self.lvl = lvl
        self.nome = nome
        if nome is None:
            self.nome = especie

        if lvl is None:
            self.lvl = random.randint(1, 100)

    def __str__(self):
        return f'{self.nome} nv:{self.lvl}'

    def atacar(self):
        return f'{self} atacou.'


class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'


class PokemonFogo(Pokemon):
    tipo = 'Fogo'


class PokemonAgua(Pokemon):
    tipo = 'Agua'




