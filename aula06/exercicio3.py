largura = float(input("Entre com a largura: "))
comprimento = float(input("Entre com o comprimento: "))
lata = float(input("Tamanho da lata de tinta (1, 3.7 ou 18 litros): "))
altura = 2.8
porta = 0.8 * 2.1
pintura = 3

area = ((2 * (largura * altura)) + (2 * (comprimento * altura))) - porta
litros = area / pintura

latas = int(litros / lata)
if latas < (litros / lata):
    latas = latas + 1

print(f"Área total: {area} m2.")
print(f"Precisa de {latas} de {lata} litros de tinta.")