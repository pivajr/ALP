with open("frutas.txt", "w", encoding="utf-8") as arquivo:
    while True:
        fruta = input("Digite uma fruta:")
        if fruta.lower() == 'sair':
           break
        else:
           arquivo.write(fruta)
           arquivo.write("\n")
