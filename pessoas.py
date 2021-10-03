from pokemon import *

class Pessoa:
    def __init__(self, nome=None, pokemons=None):
        if pokemons is None:
            pokemons = []
        if nome:
            self.nome = nome
        else:
            self.nome = 'Anonimo'

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemon(self):
        if self.pokemons:
            print(f'{self} tem {len(self.pokemons)} pokemon')
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} não tem pokemon.')


class Player(Pessoa):
    tipo = 'player'

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou: {pokemon}!')

class Inimigo(Pessoa):
    tipo = 'inimigo'




eu = Player('')

eu.mostrar_pokemon()

pokemon_selvaegm = (PokemonEletrico('Raichu'))

eu.capturar_pokemon(pokemon_selvaegm)
eu.mostrar_pokemon()
