maior_imc = 0
menor_imc = 100
soma_altura = 0
soma_peso = 0
for k in range(1, 6):
    altura = float(input(f"Entre com a altura {k}: "))
    peso = float(input(f"Entre com o peso {k}: "))
    imc = peso / (altura * altura)
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
    soma_altura = soma_altura + altura
    soma_peso = soma_peso + peso
peso_medio = soma_peso / 5
altura_media = soma_altura / 5
print("------- RESULTADOS --------------")
print(f"Altura média: {altura_media:6.2f}")
print(f"Peso médio..: {peso_medio:6.2f}")
print(f"Maior IMC...: {maior_imc:6.2f}")
print(f"Menor IMC...: {menor_imc:6.2f}")
print("---------------------------------")