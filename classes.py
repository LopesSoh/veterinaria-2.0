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

    def atualizar(pets):
        if len(pets) == 0:
            print("Nenhum animal cadastrado!")
            return

        # Listar pets
        for chave, valor in Animal.pets.items():
            print(f"{chave}° - \t{valor.get_nome()}\n\t{valor.get_raca()}\n\t{valor.get_cor()}\n\t{valor.get_peso()}")

        # Escolher pet
        alterar = int(input("Informe o ID do pet que deseja alterar\n--> "))

        # Verificação
        if alterar < 1 or alterar >= Animal.id_pets:
            print("ID inválido!")
            return

        pet = pets[alterar]

        # Escolher característica
        print("Qual característica quer alterar?")
        print("1 - Nome\n2 - Raça\n3 - Cor\n4 - Peso\n5 - Idade\n6 - Dono")
        caracteristica = int(input("--> "))

        if caracteristica == 1:
            pet.set_nome(input("Informe o novo nome do PET\n--> "))
        elif caracteristica == 2:
            pet.set_raca(input("Informe a nova raça do PET\n--> "))
        elif caracteristica == 3:
            pet.set_cor(input("Informe a nova cor do PET\n--> "))
        elif caracteristica == 4:
            pet.set_peso(input("Informe o novo peso do PET\n--> "))
        elif caracteristica == 5:
            pet.set_idade(input("Informe a nova idade do PET\n--> "))
        elif caracteristica == 6:
            pet.set_dono(input("Informe o novo dono do PET\n--> "))
        else:
            print("Opção inválida!")
            return

    # Listar novamente
    print("\n=== PET ATUALIZADO ===")
    for chave, valor in pets.items():
        print(f"{chave}° - {valor.get_nome()} ({valor.get_raca()})")    

class Gato (Animal):
    def miar (self):
        print('miau miau')

class Cachorro (Animal):
    
    def miar (self):
        print('miau miau')

class Passaro (Animal):

    def piar (self):
        print('piu piu')
    