presidentes = {
    'Deodoro':1889,
    'Prudente':1894,
    'Washington':1926,
    'Vargas':1930,
    'Janio':1961
}
print("tamanho:", len(presidentes))
dic_logico = {0: True, 1: False, 3:True}
print("all: ", all(dic_logico))
print("any:", any(dic_logico))
print(sorted(presidentes))
print(sorted(presidentes, reverse=True))
print(sorted(presidentes.values()))
print(sorted(presidentes.items()))