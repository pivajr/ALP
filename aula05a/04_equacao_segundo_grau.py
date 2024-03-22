import math

print('Cálculo de equação de Segundo Grau')
print('ax2 + bx + c = 0')
valorA = float(input('Informe o valor de a : '))
valorB = float(input('Informe o valor de b : '))
valorC = float(input('Informe o valor de c : '))

# Verifica se é uma equação de segundo grau
if (valorA == 0):
    print('Os valores não formam uma equação de segundo grau')
else:
    # Calcula o Delta
    delta = math.pow(valorB, 2) - (4 * valorA * valorC)

    if (delta < 0):
        print('A equação não possui valores reais.')
    elif (delta == 0):
        print('A equação possui apenas uma raiz')
        raiz = -(valorB) / (2 * valorA)
        print('Raiz:', raiz)
    else:
        print('A equação possui duas raizes')
        raiz1 = (-(valorB) + math.sqrt(delta)) / (2 * valorA)
        raiz2 = (-(valorB) - math.sqrt(delta)) / (2 * valorA)
        print('Raiz 1:', raiz1)
        print('Raiz 2:', raiz2)
