# Solicita informacoes
tipo_combustivel = input('Informe (A) p/ Alcool ou (G) p/ Gasolina: ').upper()
quantidade_litros = float(input('Informe a quantidade de litros: '))

# Define o valor e os descontos
if (tipo_combustivel == 'A'):
    valor = 1.9
    if (quantidade_litros <= 20):
        desconto = 3
    else:
        desconto = 5
else:
    valor = 2.5
    if (quantidade_litros <= 20):
        desconto = 4
    else:
        desconto = 6

# Calcula o total
total_pagar = (valor * quantidade_litros) * ((100 - desconto) / 100.0)

print(f'Total a pagar: {total_pagar:.2f}')
