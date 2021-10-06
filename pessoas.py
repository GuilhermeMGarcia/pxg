import random

from pokemon import *


NOME = ['Diego', 'Joao', 'Gui', 'Patricia', 'Gary', 'Ashley',
        'OCobra', 'Gu', 'Thiago'
]

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Charizard'),
    PokemonFogo('Charmilion'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Magikarp')
]


class Pessoa:
    def __init__(self, nome=None, pokemons=None):
        self.nome = nome
        if pokemons is None:
            pokemons = []
        self.pokemons = pokemons
        if nome is None:
            self.nome = random.choice(NOME)

    def __str__(self):
        return self.nome

    def mostrar_pokemon(self):
        if self.pokemons:
            print(f'{self} tem {len(self.pokemons)} pokemon')
            for indice,pokemon in enumerate(self.pokemons):
                print(f'{indice+1}-{pokemon}')
        else:
            print(f'{self} não tem pokemon.')

    def escolher_pokemon(self):
        self.mostrar_pokemon()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha seu pokemon!:'))
                    pokemon_escolhido = self.pokemons[escolha - 1]
                    print(f'Eu escolho vc {pokemon_escolhido}')
                    return pokemon_escolhido
                except:
                    print('Por favor esolha um pokemon.')
        else:
            print('Jogador n tem pokemon.')

    def batalhar(self, pessoa):
        print(f'{self} incinou batalha com {pessoa}!')
        pessoa.mostrar_pokemon()
        pessoa.escolher_pokemon()
        self.escolher_pokemon()



class Player(Pessoa):
    tipo = 'player'

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou: {pokemon}!')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if pokemons is None:
            pokemons = []
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}!')
            return pokemon_escolhido
        else:
            print('Jogador n tem pokemon.')
