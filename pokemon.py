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

        self.atack = self.lvl * 4
        self.vida = self.lvl * 10
        self.defesa = self.lvl * 2

    def __str__(self):
        return f'{self.nome} nv:{self.lvl}'

    def atacar(self, pokemon):
        atack_efetivo = int(self.atack * random.random() * 1.3)
        if atack_efetivo > pokemon.defesa:
            atack_livre = atack_efetivo - pokemon.defesa
            if atack_livre > pokemon.vida:
                imprimir = f'{pokemon} perdeu {pokemon.vida} de vida.'
            else:
                imprimir = f'{pokemon} com def:{pokemon.defesa} perdeu {atack_livre} de vida.'
            print(imprimir)
            pokemon.vida -= atack_livre
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
        print('--------------------------------------------------')
        print(f'{self} lançou um raio em {pokemon}')
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = 'Fogo'

    def atacar(self, pokemon):
        print('--------------------------------------------------')
        print(f'{self} lançou uma bola de fogoem {pokemon}')
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = 'Agua'

    def atacar(self, pokemon):
        print('--------------------------------------------------')
        print(f'{self} lançou um jato de agua em {pokemon}')
        return super().atacar(pokemon)
