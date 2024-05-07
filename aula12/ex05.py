#Aqui vamos testar as funções...

from funcoes import segundos

h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))

print(f"O total de segundos é {segundos(h,m,s)}")