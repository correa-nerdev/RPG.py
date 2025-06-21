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
visita = False
talk = ""
def aldeao():
    if visita == False :
        visita == True
        os.system('cls') 
        print("Vejo que você é novo por aqui!")
        print("")
        print("O que você deseja?")
        print("________________________________________________________________________________")
        print("1. Quest")
        print("2. Adeus...")
        print("________________________________________________________________________________")
        talk = input("=>  ")
        
        if talk == 1:
            os.system('cls')
            print("Quest:")
            print("1. Mate ")



# Monstros do mapa 
goblin = {
    "name": "Goblin",
    "hp": 5,
    "forca": 1,
    "exp": 5,
}
lobo_Selvagem = {
    "name": "Lobo Selvagem",
    "hp": 7,
    "forca": 3,
    "exp": 7,
}
morcego = {
    "name": "Morcego",
    "hp": 3,
    "forca": 1,
    "exp": 2,
}
esqueleto = {
    "name": "Esqueleto",
    "hp": 4,
    "forca": 2,
    "exp": 6,
}
pivete = {
    "name": "Pivete",
    "hp": 10,
    "forca": 3,
    "exp": 15,
}
bandidos = {
    "name": "Bandidos",
    "hp": 15,
    "forca": 5,
    "exp": 20,
}

# Mapas
mapas = {
    "Deep Florest": {
        "descricao": "Uma floresta densa e sombria, cheia de árvores altas e arbustos espinhosos.",
        "monstros": [goblin, lobo_Selvagem]
    },
    
    "Cave": {
        "descricao": "Uma caverna úmida e escura, com estalactites penduradas no teto.",
        "monstros": [morcego, esqueleto]
    },

    "Village": {
        "descricao": "Uma pequena vila com casas de madeira e um mercado movimentado.",
        "monstros": [pivete, bandidos],
        "npc": ["aldeao"]
    }
}


# Funçao para entrar nos mapas
deep_florest = ''
cave = ''
village = ''

def mapa():
    global deep_florest, cave, village
    deep_florest = False
    cave = False
    village = False
    os.system('cls')
    print("________________________________________________________________")
    print("Mapas disponíveis:")
    print("________________________________________________________________")
    for mapa in mapas:
        print(f"- {mapa}")
    print("________________________________________________________________")
    print("")
    print("Para viajar, digite o nome de algum lugar. Se você deseja fechar o maa, digite 'Fechar'")
    print("")
    acao = input("=>  ").lower()
    
    def entrar(acao):
        global deep_florest, cave, village
        if acao == "deep florest":
            deep_florest = True
            cave = False
            village = False
        elif acao == "cave":
            deep_florest = False
            cave = True
            village = False
        elif acao == "village":
            deep_florest = False
            cave = False
            village = True

    entrar(acao)
    interface()

# Funçoes de luta
def lutar():
    print("Abacate")
    

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
    print("4. 'sair' - Sai do jogo")
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
    elif acao == "sair":
        return "..."
    else:
        print("Digite uma ação válida")
        interface()
    

lore()