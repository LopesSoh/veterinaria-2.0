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

        if tipo == 1:
                pet = Gato(nome, peso, idade, raca, cor, dono)
        elif tipo == 2:
                pet = Cachorro(nome, peso, idade, raca, cor, dono)
        elif tipo == 3:
                pet = Passaro(nome, peso, idade, raca, cor, dono)
        else:
            print("Tipo inválido!")
            continue

        Animal.cadastro(pet)
        print("Cadastro realizado com sucesso!")
        Animal.L_e_P()

    elif resp == 2:
        Animal.L_e_P()
        Animal.listar(pets)
        Animal.L_e_P()

    else:
        print("Opção inválida!")




