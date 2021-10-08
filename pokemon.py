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

        self.atack = self.lvl * 2.5
        self.vida = self.lvl * 10
        self.defesa = self.lvl * 1.3

    def __str__(self):
        return f'{self.nome} nv:{self.lvl}'

    def atacar(self, pokemon):
        print('--------------------------------------------------')
        if self.atack > pokemon.defesa:
            self.atack = self.atack - pokemon.defesa
            if self.atack > pokemon.vida:
                imprimir = f'{pokemon} perdeu {pokemon.vida} de vida.'
            else:
                imprimir = f'{pokemon} perdeu {self.atack} de vida.'
            print(imprimir)
            pokemon.vida = pokemon.vida - self.atack
        else:
            print(f'{pokemon} com def:{pokemon.defesa} não sofreu dano.')

        if pokemon.vida <=0:
            print(f'{pokemon} foi derrotado.')
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'

    def atacar(self, pokemon):
        print(f'{self} lançou um raio de {self.atack} dano em {pokemon}')
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = 'Fogo'

    def atacar(self, pokemon):
        print(f'{self} lançou uma bola de fogo de {self.atack} dano em {pokemon}')
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = 'Agua'

    def atacar(self, pokemon):
        print(f'{self} lançou um jato de agua de {self.atack} dano em {pokemon}')
        return super().atacar(pokemon)
