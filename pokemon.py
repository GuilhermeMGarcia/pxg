class Pokemon:

    def __init__(self, especie, lvl=1, nome=None):
        self.especie = especie
        self.lvl = lvl

        if nome:
            self.nome = nome
        else:
            self.nome = especie

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






