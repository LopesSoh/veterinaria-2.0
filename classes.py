class Animal:
    def __init__(self, nome, peso, idade, raca, cor, dono):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__raca = raca
        self.__cor = cor
        self.__dono = dono


class Gato (Animal):

    #modulo de controle
    def __init__(self, nome, peso, idade, raca, cor, dono):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__raca = raca
        self.__cor = cor
        self.__dono = dono

    def miar (self):
        print('miau miau')

class Cachorro (Animal):

    #modulo de controle
    def __init__(self, __nome, __peso, __idade, __raca, __cor, __dono):
        self.nome = __nome
        self.peso = __peso
        self.idade = __idade
        self.raca = __raca
        self.cor = __cor
        self.dono = __dono
    
    def miar (self):
        print('miau miau')

class Passaro (Animal):
        
    def __init__(self, __nome, __peso, __idade, __especie, __cor, __dono):
        self.nome = __nome
        self.peso = __peso
        self.idade = __idade
        self.especie = __especie
        self.cor = __cor
        self.dono = __dono

    def piar (self):
        print('piu piu')
    