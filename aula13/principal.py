# Importação das Funções
from valida_cpf import valida_cpf
from valida_data import valida_data
from exibir_menu import exibir_menu

# Script principal
while True:
    escolha = exibir_menu()

    if escolha == 1:  # Cadastrar
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        cpf = input("Digite o CPF (no formato xxx.xxx.xxx-xx): ")

        # Validar CPF
        while (not valida_cpf(cpf)):
            print("CPF inválido. Tente novamente.")
            cpf = input("Digite o CPF (no formato xxx.xxx.xxx-xx): ")

        data_nascimento = input("Digite a data de nascimento (no formato dd/mm/aaaa): ")

        # Validar data de nascimento
        while (not valida_data(data_nascimento)):
            print("Data de nascimento inválida. Tente novamente.")
            data_nascimento = input("Digite a data de nascimento (no formato dd/mm/aaaa): ")

        renda_bruta = float(input("Digite a renda bruta: R$ "))

        # Realizar o cadastro ou salvar os dados conforme necessário
        print("Cadastro realizado com sucesso!")

    elif escolha == 2:  # Exibir Mensagem
        mensagens = [
            "A persistência realiza o impossível",
            "Seus sonhos não precisam de plateia, eles só precisam de você",
            "A persistência é o caminho do êxito",
            "No meio da dificuldade encontra-se a oportunidade"
        ]
        import random
        mensagem = random.choice(mensagens)
        print(f"Mensagem Motivacional: {mensagem}")

    elif escolha == 3:  # Sair
        print("Bye bye!")
        break