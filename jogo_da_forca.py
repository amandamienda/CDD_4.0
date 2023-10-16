def forca (erros):
    print("  __________  ")
    print(" |.       |    ")
    if (erros == 1):
        print(" |.       @  ")

    if (erros == 2):
        print(" |.       @   ")
        print(" |.      /     ")

    if (erros == 3):
        print(" |.       @   ")
        print(" |.      /|    ")


    if (erros == 4):
        print(" |.      @    ")
        print(" |.      /|\   ")


    if (erros == 5):
        print(" |.       @    ")
        print(" |.      /|\   ")
        print(" |.       |    ")


    if (erros == 6):
        print(" |.       @    ")
        print(" |.      /|\   ")
        print(" |.       |    ")
        print(" |.      /     ")

    if (erros == 7):
        print(" |.       @    ")
        print(" |.      /|\   ")
        print(" |.       |    ")
        print(" |.      / \   ")

    print(" |.            ")
    print()
palavra = "amanda"
letrasUsuario = []
erros = 0
chance = 7
ganhou = False

while True:
    for letra in palavra:
        if letra in letrasUsuario:
            print(letra, end="")
        else:
            print("_", end=" ")

    print()
    print(f"Você tem {chance} chances.")
    tentativa = input("Digite uma letra: ")
    letrasUsuario.append(tentativa)
    if tentativa not in palavra:
        chance -= 1
        erros += 1
        forca(erros)

    ganhou = True
    for letra in palavra:
        if letra not in letrasUsuario:
            ganhou = False

    if chance == 0 or ganhou:
        print(f"Você perdeu! :( A palavra era {palavra}")
        break