valor = float(input("Entre com o valor da compra: "))
if valor <= 1000:
    desconto = 10
elif valor <= 5000:
    desconto = 20
else:
    desconto = 30

valor_desconto = (valor * desconto) / 100
novo_valor = valor - valor_desconto
print(f"Valor da Compra......: {valor:8.2f}")
print(f"Valor do Desconto....: {valor_desconto:8.2f} --> {desconto}%")
print(f"Valor Final da Compra: {novo_valor:8.2f}")