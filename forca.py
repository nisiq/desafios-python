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
acertos = 0
erros = 0
letras_corretas = ''
letras_erradas = ''

print(len(palavra_nutella))

print("-="*30)
print("Olá jogador! Te desafio a acertar qual palavra eu estou pensando!")
print("Dica inicial: A palavra trata-se de um lugar!")

while acertos != len(palavra_nutella) and erros != 6:
    mensagem = ''
    for letra in palavra_nutella:
        if letra in letras_corretas:
            mensagem += letra
        else:
            mensagem += '_'
    print(mensagem)
    letra = input("Digite UMA letra: ").upper()
    print("=-" * 30)
    if len(letra) > 1:
        print("\33[1mERROR 401 - Unauthorized.\033[1m Atenção jogador, é permitido apenas UMA letra por jogada.")
    else:
        if letra in palavra_nutella:
            print("\033[0;30;42mVocê acertou a letra! Continue assim!\033[m")
            letras_corretas += letra
            acertos += 1
        else:
            print("\033[0;30;41mVocê errou a letra! Cuidado com as chances...\033[m")
            letras_erradas += letra
            erros += 1
        print(f"Letras corretas já digitadas: {letras_corretas}")
        print(f"Letras erradas já digitadas: {letras_erradas}")
