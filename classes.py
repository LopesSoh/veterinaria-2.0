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


#GETS    
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
    

#SETS
    def set_nome(self, nome): 
        self.__nome = nome

    def set_peso(self, peso): 
        self.__peso = peso

    def set_idade(self, idade): 
        self.__idade = idade

    def set_raca(self, raca): 
        self.__raca = raca

    def set_cor(self, cor): 
        self.__cor = cor

    def set_dono(self, dono): 
        self.__dono = dono
    

    #Funções
    def cadastro(pet):
        Animal.pets[Animal.id_pets] = pet
        Animal.id_pets += 1

    def listar():
        for chave, valor in Animal.pets.items():
            print(f"{chave}° - \t{valor.get_nome()}\n\t{valor.get_raca()}\n\t{valor.get_cor()}\n\t{valor.get_peso()}")

    def menu():
        print("--MENU--")
        print(" 1 - Realizar Cadastro \n 2 - Listar Cadastrados \n 0 - Sair")

    def L_e_P():
        os.system("pause")
        os.system("cls")

    def menu_cadastro():
        print("--- CADASTRO DE ANIMAL ---")
        print("Selecione:\n1 - Gato\n2 - Cachorro\n3 - Pássaro")

class Gato (Animal):
    def miar (self):
        print('miau miau')

class Cachorro (Animal):
    
    def miar (self):
        print('miau miau')

class Passaro (Animal):

    def piar (self):
        print('piu piu')
    