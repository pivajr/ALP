v = 0
frase = input("Digite a frase: ")
for letra in frase:
    if letra.upper() in "AEIOU":
        v = v + 1

print(f"A frase têm {v} vogal(is).")