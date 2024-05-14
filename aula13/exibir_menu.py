def exibir_menu():
    while True:
        print("Menu de Opções:")
        print("1 - Cadastrar")
        print("2 - Exibir Frase")
        print("3 - Sair")

        opcao = input("Digite a opção desejada: ")

        # Verificar se a opção é um número
        if not opcao.isdigit():
            print("Por favor, digite um número válido.")
            continue

        # Converter a opção para inteiro
        opcao = int(opcao)

        # Verificar se a opção está dentro do intervalo válido
        if 1 <= opcao <= 3:
            return opcao
        else:
            print("Opção inválida. Digite um número entre 1 e 3.")
            continue
