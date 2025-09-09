class Animal:
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



class Gato (Animal):

    #modulo de controle
    def __init__(self, nome, peso, idade, raca, cor, dono):
        Animal.__init__(self, nome, peso, idade, raca, cor, dono)

    def miar (self):
        print('miau miau')

class Cachorro (Animal):

    #modulo de controle
    def __init__(self, nome, peso, idade, raca, cor, dono):
        Animal.__init__(self, nome, peso, idade, raca, cor, dono)
    
    def miar (self):
        print('miau miau')

class Passaro (Animal):
        
    def __init__(self, nome, peso, idade, raca, cor, dono):
        Animal.__init__(self, nome, peso, idade, raca, cor, dono)

    def piar (self):
        print('piu piu')
    