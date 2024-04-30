# Inicializa um dicionário vazio
idade_por_sobrenome = {}

# Preenche o dicionário com 10 elementos
for _ in range(3):
   sobrenome = input("Digite o sobrenome da pessoa: ")
   idade = int(input("Digite a idade da pessoa: "))
   idade_por_sobrenome[sobrenome] = idade

# Encontra o sobrenome da pessoa mais velha
sobrenome_mais_velho = max(idade_por_sobrenome, key=idade_por_sobrenome.get)

# Exibe o resultado
print(f"\nO sobrenome da pessoa mais velha é: {sobrenome_mais_velho}")
