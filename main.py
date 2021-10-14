import pickle

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


def salvar_jogo(player):
    arquivo = "database.db"
    try:
        with open(arquivo, "wb") as obj_arquivo:
            pickle.dump(arquivo, obj_arquivo)
            print('Jogo salvo com sucesso')
    except Exception as error:
        print('Erro ao Salvar o jogo')
        print(error)


def carregar_jogo(player):
    arquivo = "database.db"
    try:
        with open(arquivo, "rb") as obj_arquivo:
            player = pickle.load(obj_arquivo)
            return player
            print('Jogo salvo com sucesso')
    except Exception as error:
        print('Erro ao Carregar o jogo')
        print(error)


if __name__ == "__main__":
    print('-------------------------------------')
    print('Seja bem vindo ao PXG')
    print('-------------------------------------')

    nome = input('Digite seu nome:')
    player = Player(nome)
    print(f'{nome} parabens, esse é o mundo dos pokemons, voce tera que explorar'
          f' e se tornar o mestre dos pokemons')
    player.mostra_dinheiro()

    print('Capture o maximo de pokemons que conseguir')
    if player.pokemons:
        print('Vi que voce ja possui pokemon')
        player.mostrar_pokemon()
    else:
        print('Voce n possui pokemon agora voce podera escolher um')
        escolher_pokemon(player)

    print('Pronto, agora que vc possui um pokemon tera que lutar contra Gary seu amigo de infancia')
    gary = Inimigo('Gary', [PokemonAgua('squirtle', 1)])
    player.batalhar(gary)

    while True:
        print('--------------------------')
        print('Oque deseja fazer')
        print('1- Explorar o mundo')
        print('2- Batalhar com inimigo')
        print('3- Mostrar dinheiro')
        print('4- Mostrar Pokemons')
        print('5- Salvar Jogo')
        print('6- Carregar Jogo')
        print('0- Sair do jogo')
        escolha = input('Escolha:')

        if escolha == '0':
            print('Fecando o jogo...')
            break
        elif escolha == '1':
            player.exlorar()
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
        elif escolha == '3':
            player.mostra_dinheiro()
        elif escolha == '4':
            player.mostrar_pokemon()
        elif escolha == '5':
            salvar_jogo(player)
        elif escolha == '6':
            carregar_jogo(player)
        else:
            print('Escolha invalida')


