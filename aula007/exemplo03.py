qtd = 0
frase = input("Digite uma frase: ")
for letra in frase:
    if letra in 'AEIOUaeiouãíóúáàéü':
        qtd = qtd + 1
print(f"Existem {qtd} vogais na frase.")