from random import choice

def obter_escolha_computador():
    escolhas = ["pedra", "papel", "tesoura"]
    return choice(escolhas)

def obter_vencedor(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
        return "Empate"
    elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
            (escolha_jogador == "papel" and escolha_computador == "pedra") or \
            (escolha_jogador == "tesoura" and escolha_computador == "papel"):
        return "Jogador"
    else:
        return "Computador"


print("Bem-vindo ao jogo Tesoura, Papel e Pedra!")
while True:
    escolha_jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar o jogo): ").lower()
    if escolha_jogador == 'sair':
        print("Obrigado por jogar! Agora, vá estudar!!")
        break
    if escolha_jogador not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida! Tente novamente.")
        continue

    escolha_computador = obter_escolha_computador()
    print(f"Computador escolheu: {escolha_computador}")

    vencedor = obter_vencedor(escolha_jogador, escolha_computador)
    if vencedor == "Empate":
        print("É um empate!")
    elif vencedor == "Jogador":
        print("Você venceu!")
    else:
        print("Você perdeu!")

