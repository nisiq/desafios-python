#28.02.2023 - Sorteie um número primo entre 0 e 1000 e o usuário deve adivinhar qual número é, através de dicas (maior/menor)

from random import randint

while True:
    computador = randint(0, 1000)
    de = 0
    print("Olá usuário, acabei de sortear um número primo entre 0 e 1000.")
    print("Te desafio a acertar qual foi...")

    for i in range(1, computador):
        if computador % i == 0:
            de += 1
        if de == 2:
            break
        
print(computador)
        
acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Dê seu palpite: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Pensei em um número maior, tente novamente!")
        elif jogador > computador:
            print("Pensei em um número menor, tente novamente!")
                     
print("Parabéns usuário! Você acertou com {} tentativas!".format(palpites))

===================================================
#1º SORTEAR UM NÚMERO ENTRE 0 E 1000 (PRIMO)
#2º DAR DICA (MAIOR OU MENOR)
#3º CHANCES = 15
#4º VIDA 1.000
#5º TEMPO PARA JOGAR = 60 SEGUNDOS -> datetime.datetime.now()

from random import randint

print("Olá usuário, acabei de sortear um número primo entre 0 e 1000.")

computador = randint(1, 1000)

def primeNumber():
    isPrime = False
    while isPrime == False:
        for count in range(2, computador - 1):
            if computador % count == 0:
                break
            else:
                isPrime = True
                continue
    return computador

acertou = False
palpites = 0
computador = randint(1, 1000)

while acertou:
    palpites += 1
    if jogador == computador:
        acertou = True
        break
    else:
        if jogador < computador:
            print("Pensei em um número maior, tente novamente!")
        elif jogador > computador:
            print("Pensei em um número menor, tente novamente!")

    print("Parabéns usuário! Você acertou com {} tentativas!".format(palpites+1))


import random
import datetime

i = 0

while i==0:
    mult = 0
    sorteado = random.randint(1, 1000)
    for count in range(2, sorteado):
        if (sorteado % count == 0):
            mult += 1
    if (mult==0):
        i += 1

escolhido = 0
chances = 15
vida = 1000
dif_vida = sorteado - escolhido

print(f"Você tem {vida} vidas!")

while escolhido != sorteado:

    escolhido = int(input("Seu palpite: "))

    if escolhido % 2 == 0:
        print("Você perdeu {} vidas".format(vida-dif_vida))

    if escolhido > sorteado:
        print("O número é menor")

    elif escolhido < sorteado:
        print("O número é maior")
        
print("Parabéns! Você acertou!")



