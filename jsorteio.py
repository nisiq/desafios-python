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
