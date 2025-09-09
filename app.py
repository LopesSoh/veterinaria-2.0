from classes import*

while True:
    Animal.menu()
    resp = int(input("--> "))
    
    if resp == 1:
        Animal.L_e_P()
        Animal.menu_cadastro()
        tipo = int(input("--> "))

        nome = input("Nome: ")
        peso = input("Peso: ")
        idade = input("Idade: ")
        raca = input("Raça ou espécie: ")
        cor = input("Cor: ")
        dono = input("Nome do dono: ")






Animal.menu()
resp1 = int(input("--> "))

while resp1 != 0:
    if resp1 == 1:
        limpar_e_pausar()
        menu_cadastro()
        tipo = int(input("--> "))
        limpar_e_pausar()

        print("Preencha as informações do animal:")
        nome = input("Nome: ")
        peso = input("Peso: ")
        idade = input("Idade: ")
        raca_ou_especie = input("Raça ou especie:")
        cor = input("Cor: ")
        dono = input("Nome do dono:")

        cadastro(tipo, nome, peso, idade, raca_ou_especie, cor, dono)
        print("Cadastro realizado com sucesso!")
    
    else:
        print(" ")