from pessoas import *


def escolher_pokemon(player):
    print(f'Ola {player} agora vc podera escolher 1 pokemon para te acompanhar!')

    pikachu = PokemonEletrico('Pikachu', 1)
    charmander = PokemonFogo('charmander', 1)
    squirtle = PokemonAgua('Squirtle', 1)

    while True:
        print(f'1- {pikachu}')
        print(f'2- {charmander}')
        print(f'3- {squirtle}')

        escolha = input('Escolha um pokemon:')
        if escolha == '1':
            player.capturar_pokemon(pikachu)
            break
        if escolha == '2':
            player.capturar_pokemon(charmander)
            break
        if escolha == '3':
            player.capturar_pokemon(squirtle)
            break
        else:
            print('Escolha um pokemon!')


player = Player()
player.mostra_dinheiro()
escolher_pokemon(player)
player.mostrar_pokemon()
inimigo = Inimigo(nome=None, pokemons=[PokemonEletrico('Raichu', lvl=1)])
player.batalhar(inimigo)

