import random

palavras = ('elefante', 'pantera', 'cervo', 'polvo', 'ornitorrinco')
dicas = ['Animal de grande porte e tromba',
         'Animal felino preto',
         'Animal com chifres ramificados',
         'Animal marinho com 8 tentáculos',
         'Animal mamífero com bico de pato']

palavra_sort = random.choice(palavras).upper()
vidas = 6

letras_descobertas = ["_"] * len(palavra_sort)

while vidas > 0:
    print(" ".join(letras_descobertas)) # Exibe as letras já descobertas separadas por espaços
    letra = input('Digite uma letra: ').upper()

    posicoes = []

    for i, char in enumerate(palavra_sort):
        if char == letra:
            posicoes.append(i)
            letras_descobertas[i] = letra # Substitui o traço pela letra correspondente na posição i

    if posicoes:
        print(f"A letra '{letra}' aparece nas posições da palavra sorteada.")
    else:
        vidas -= 1
        if vidas > 0:
            palavra_index = palavras.index(palavra_sort.lower()) # Obtém o índice da palavra sorteada na lista "palavras"
            dica = dicas[palavra_index] # Obtém a dica correspondente usando o mesmo índice na lista "dicas"
            print(f"A letra '{letra}' não aparece na palavra sorteada. Você perdeu uma vida. Restam {vidas} vidas.")
            print(f"Dica: {dica}")
        else:
            print(f"A letra '{letra}' não aparece na palavra sorteada '{palavra_sort}.' Você perdeu todas as vidas. Fim de jogo.")
            break

    if "_" not in letras_descobertas:
        print(f"Parabéns, você descobriu a palavra '{palavra_sort}'!")
        break

         
         
====================================================== 
         
         
 palavra_nutella = "Gym".upper()

print(len(palavra_nutella))

print("-="*30)
print("Olá jogador! Te desafio a acertar qual palavra eu estou pensando!")
print("Dica inicial: A palavra trata-se de um lugar e está escrita em inglês!")

letra = input("Digite UMA letra: ").upper()
if len(letra)>1:
    print("ERROR 401 - Unauthorized. Atenção jogador. É permitido apenas UMA letra por jogada.")
else:
    if letra in palavra_nutella:
        print("Você acertou a letra! Continue assim!")
    else:
        print("Você errou a letra! Cuidado com as chances...")
