import os
from classes import*

id_pets = 1

#dicionario dos pets
pets = {}

#função menu
def menu():
    print("--MENU-- \n Digite a opção desejada: \n 1-Realizar Cadastro \n 2-Atualizar Cadastro \n 3-Listar Cadastrados \n 0-Sair")

#função limpar e pausar tela
def limpar_e_pausar():
    os.system('pause')
    os.system('cls')

def menu_cadastro():
    print("Selecione:\n 1-Gato \n 2-Cachorro \n 3-Passaro")


def cadastro(pets, tipo, nome, peso, idade, raca_ou_especie, cor, dono):
    global id_pets
    if tipo == 1:
        pets[id_pets] = Gato(nome, peso, idade, raca_ou_especie, cor, dono)
    elif tipo == 2:
        pets[id_pets] = Cachorro(nome, peso, idade, raca_ou_especie, cor, dono)
    elif tipo == 3:
        pets[id_pets] = Passaro(nome, peso, idade, raca_ou_especie, cor, dono)
    id_pets += 1

