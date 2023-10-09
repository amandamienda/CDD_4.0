A = []
num = 0
contador = 0
while contador < 10:
    if num % 2 != 0:
        A.append(num)
        contador += 1
    num += 1

print(A)