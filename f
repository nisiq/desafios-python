from random import randint

i = 0

while i==0:
    mult = 0
    computador = randint(1, 1000)
    for count in range(2, computador):
        if (computador % count == 0):
            mult += 1
    if (mult==0):
        i += 1

print("Olá usuário, acabei de pensar em um número entre 0 e 1000.")
print("Será que você é capaz de adivinhar? ")

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Digite seu palpite: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Eu pensei em um número maior. Tente novamente!")
        elif jogador > computador:
            print("Eu pensei em um número menor. Tente novamente!")

print(f"Parabéns! Você acertou com {palpites} tentativas. Parabéns!")
