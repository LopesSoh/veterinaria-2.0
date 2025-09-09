import os

class Animal:
    id_pets = 1
    pets = {}

    def __init__(self, nome, peso, idade, raca, cor, dono):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__raca = raca
        self.__cor = cor
        self.__dono = dono
    
    def get_nome(self):
        return self.__nome

    def get_peso(self):
        return self.__peso

    def get_idade(self):
        return self.__idade

    def get_raca(self):
        return self.__raca

    def get_cor(self):
        return self.__cor

    def get_dono(self):
        return self.__dono
    

    #Funções
    def cadastro(pet):
        Animal.pets[Animal.id_pets] = pet
        Animal.id_pets += 1

    def listar():
        for chave, valor in Animal.items():
            print(f"{chave}° - \t{valor.getNome()}\n\t{valor.getRaca()}\n\t{valor.getCor()}\n\t{valor.getPeso()}")

    def menu():
        print("--MENU--")
        print(" 1 - Realizar Cadastro \n 2 - Listar Cadastrados \n 0 - Sair")

    def L_e_P():
        os.system("pause")
        os.system("cls")


class Gato (Animal):
    def miar (self):
        print('miau miau')

class Cachorro (Animal):
    
    def miar (self):
        print('miau miau')

class Passaro (Animal):

    def piar (self):
        print('piu piu')
    