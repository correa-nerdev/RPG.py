# Imports
import random
import os

# Pega o nome do player e inicia o jogo
os.system('cls') 
print( "Bem vindo, grande herói!")
print("")
input_name = input("Por favor, digite seu nome: ")
os.system('cls') 


#variaveis globais
exp = 0
max_hp = 10
hp = max_hp
forca = 1
level = 1
name = input_name
max_exp = level * 10

# Criação do player
player = {
    "name": name,
    "level": level,
    "exp": exp,
    "max_exp": max_exp,
    "hp": hp,
    "max_hp": hp,
    "forca": forca,
    "inventory": [],
}
#funcao de lvl up
def lvl_up(player):
    if player['exp'] >= max_exp:
        player['level'] += 1
        player['exp'] = 0
        player['max_hp'] += 5
        player['hp'] = player['max_hp']
        player['forca'] += 1

# Lore do jogo
def lore():
    os.system('cls')
    print("")
    input("Você acorda no meio de uma floresta escura e silenciosa...") 
    print("")
    input("Você não se lembra de como chegou lá, mas sente uma estranha sensação...")
    print("________________________________________________________________________________")
    print("")
    input("Pressione Enter para continuar...")
    interface()


# Funcoes de interação
# NPCs

# Monstros do mapa 
Goblin = {
    "name": "Goblin",
    "hp": 5,
    "forca": 1,
    "exp": 5,
}
Lobo_Selvagem = {
    "name": "Lobo Selvagem",
    "hp": 7,
    "forca": 3,
    "exp": 7,
}
Morcego = {
    "name": "Morcego",
    "hp": 3,
    "forca": 1,
    "exp": 2,
}
Esqueleto = {
    "name": "Esqueleto",
    "hp": 4,
    "forca": 2,
    "exp": 6,
}
Pivete = {
    "name": "Pivete",
    "hp": 10,
    "forca": 3,
    "exp": 15,
}
Bandidos = {
    "name": "Bandidos",
    "hp": 15,
    "forca": 5,
    "exp": 20,
}
# Mapas
mapas = {
    "Deep Florest": {
        "descricao": "Uma floresta densa e sombria, cheia de árvores altas e arbustos espinhosos.",
        "monstros": ["Goblin", "Lobo Selvagem"]
    },
    
    "Cave": {
        "descricao": "Uma caverna úmida e escura, com estalactites penduradas no teto.",
        "monstros": ["Morcego", "Esqueleto"]
    },

    "Village": {
        "descricao": "Uma pequena vila com casas de madeira e um mercado movimentado.",
        "monstros": ["Pivete", "Bandidos"]
    }
}


# Funçao para entrar nos mapas
def mapa():
    os.system('cls')
    print("________________________________________________________________")
    print("Mapas disponíveis:")
    print("________________________________________________________________")
    for mapa in mapas:
        print(f"- {mapa}")
    print("________________________________________________________________")
    input("Pressione Enter para voltar ao menu principal...")
    interface()

# Funçoes de luta


# Menu de status do personagem
def status():
    if acao == "status":
        os.system('cls')
        print("________________________________________________________________")
        print("Status do personagem:")
        print("________________________________________________________________")
        print(f"Nome: {player['name']}")
        print(f"Nível: {player['level']}")
        print(f"Experiência: {player['exp']}/{player['max_exp']}")
        print(f"HP: {player['hp']}/{player['max_hp']}")
        print(f"Força: {player['forca']}")
        print("________________________________________________________________")
        input("Pressione Enter para voltar ao menu principal...")
        interface()

# Menu de informações de comando
def comandos():
    os.system('cls')
    print("________________________________________________________________")
    print("Lista de comandos:")
    print("________________________________________________________________")
    print("1. 'status' - Ver status do personagem")
    print("2. 'mapa' - Verificar o mapa atual")
    print("3. 'lutar' -  Procura oponente para batalha")
    print("________________________________________________________________")
    input("Precione Enter para fechar lista de comandos...")
    interface()

# Interface
def interface():
    os.system('cls')
    print("Bem vindo ao jogo, " + player['name'] + "!")
    print("Digite 'help' para ver os comandos disponíveis.")
    global acao
    acao = input("=> ")
    if acao == "help":
        comandos()
    elif acao == "status":
        status()
    elif acao == "mapa":
        mapa()
    elif acao == "lutar":
        lutar()
    

lore()