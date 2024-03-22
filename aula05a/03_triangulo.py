print('Informe os valores dos lados do triângulo')
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

# Verifica se eh um triangulo
if (l1 > (l2 + l3)) or (l2 > (l1 + l3)) or (l3 > (l1 + l2)):
    ehTriangulo = False
else:
    ehTriangulo = True

if (ehTriangulo):
    print('Os valores formam um Triângulo')
    # Verifica o tipo de triangulo
    if (l1 == l2) and (l2 == l3):
        print('Triângulo Equilatero')
    elif (l1 == l2) or (l1 == l2) or (l2 == l3):
        print('Triângulo Isosceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Os valores não formam um Triãngulo')
