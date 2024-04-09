v = 0
frase = input("Digite a frase: ").upper()
for vogal in "AEIOU":
    v = v + frase.count(vogal)

print(f"A frase têm {v} vogal(is).")