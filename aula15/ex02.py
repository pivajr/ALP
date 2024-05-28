def probabilidade_pe(valor_carta):
    total_cartas = 40
    cartas_desejadas = 4
    prob_primeiro = cartas_desejadas / total_cartas
    return prob_primeiro


def probabilidade_mao(valor_carta):
    total_cartas = 40
    cartas_desejadas = 4
    cartas_primeiro_jogador = 3
    prob_primeiro = cartas_desejadas / total_cartas
    prob_segundo_dado_primeiro = (cartas_desejadas - 1) / (total_cartas - cartas_primeiro_jogador)
    prob_combinada = prob_primeiro * prob_segundo_dado_primeiro
    return prob_primeiro, prob_segundo_dado_primeiro, prob_combinada



carta_escolhida = input("Digite a carta desejada (A, 2, 3, 4, 5, 6, 7, Q, J, K): ").strip().upper()
if carta_escolhida not in ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']:
    print("Carta inválida.")
    return

prob_primeiro = probabilidade_pe(carta_escolhida)
prob_primeiro, prob_segundo, prob_combinada = probabilidade_pe(carta_escolhida)

print(f"Probabilidade do pé sair com a carta {carta_escolhida}: {prob_primeiro * 100:.2f}%")
print(
    f"Probabilidade do mão sair com a carta {carta_escolhida|} dado que o primeiro já a possui}: {prob_segundo * 100:.2f}%")
print(f"Probabilidade de ambos os jogadores saírem com a carta {carta_escolhida}: {prob_combinada * 100:.2f}%")

