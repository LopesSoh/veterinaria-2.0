class Gato:

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

class Cachorro:

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

class Passaro:
        
    def __init__(self, __nome, __peso, __idade, __especie, __cor, __dono):
        self.nome = __nome
        self.peso = __peso
        self.idade = __idade
        self.especie = __especie
        self.cor = __cor
        self.dono = __dono

    def piar (self):
        print('piu piu')
    