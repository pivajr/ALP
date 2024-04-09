data = input("Digite a Data dd/mm/aaa: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6::]
data_invertida = ano+mes+dia
print(data, " - ", data_invertida)