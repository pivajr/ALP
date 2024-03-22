# Chama-se ano bissexto o ano ao qual é acrescentado um dia extra,
# ficando com 366 dias, um dia a mais do que os anos normais de
# 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos
# de 100 que não são múltiplos de 400). Isto é feito com o objetivo
# de manter o calendário anual ajustado com a translação da Terra e
# com os eventos sazonais relacionados às estações do ano.
# O anterior ano bissexto foi 2020 e o próximo será 2024.

ano = int(input('Informe um ano: '))

bissexto = False
if (ano % 4 == 0):
    bissexto = True
    if (ano % 100 == 0) and (ano % 400 != 0):
        bissexto = False

if (bissexto):
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO É BISSEXTO')
