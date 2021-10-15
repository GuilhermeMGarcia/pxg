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
    def __init__(self, nome=None, pokemons=None, dinheiro=100):
        self.nome = nome
        if pokemons is None:
            pokemons = []
        self.pokemons = pokemons
        if nome is None:
            self.nome = random.choice(NOME)

        self.dinheiro = dinheiro

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
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}!')
            return pokemon_escolhido
        else:
            print('Jogador n tem pokemon.')

    def mostra_dinheiro(self):
        print(f'Voce tem ${self.dinheiro}')

    def ganhar_dinheiro(self, dinheiro):
        self.dinheiro += dinheiro
        print(f'Voce obteve ${dinheiro}')
        self.mostra_dinheiro()

    def batalhar(self, inimigo):
        print(f'{self} incinou batalha com {inimigo}!')
        inimigo.mostrar_pokemon()
        pokemon_inimigo = inimigo.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon_inimigo and pokemon:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} venceu a batalha')
                    dinheiro = pokemon_inimigo.lvl * 2
                    self.ganhar_dinheiro(dinheiro)
                    break
                vitoria_inimia = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimia:
                    print(f'{inimigo} venceu a batalha')
                    break
        else:
            print('Essa batalha n pode acontecer.')


class Player(Pessoa):
    tipo = 'player'

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou: {pokemon}!')

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

    def exlorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f'voce encontrou um {pokemon}')
            escolha = input('Deseja caprturar o pokemon s/n: ')
            if escolha == 's':
                if random.random() >= 0.5:
                    self.capturar_pokemon(pokemon)
                    print(f'parabens vc capturou {pokemon}')
                else:
                    print(f'{pokemon} fugiu!!')
            else:
                print('Boa viagem')
        else:
            print('Não encontrou nenhum pokemon.')
            return


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if pokemons is None:
            pokemons = []
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)


