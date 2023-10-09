impar = []
par = []
pos = []
neg = []

for x in range(10):
    num = int(input("Digite um número: "))

    if num % 2 != 0:
        impar.append(num)

    if num % 2 == 0:
        par.append(num)

    if num > 0:
        pos.append(num)

    else:
        neg.append(num)

print(f"Números ímpares: {impar}, números pares: {par}, números positivos: {pos} e números negativos: {neg}")