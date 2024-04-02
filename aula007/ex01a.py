n = int(input("Digite o valor de n: "))
e = 0
k = 1
while k <= n:
    e = e + 2**k
    k = k + 1

print(f"O valor de E = {e}")


