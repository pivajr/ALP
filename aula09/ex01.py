lista = []
for i in range(10):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)

print(lista[::-1])
for i in range(9, -1, -1):
    print(lista[i], end=',')
print()
lista.reverse()
print(lista)
