#inicio, fim, passo - progressão

from time import sleep

def progressao(inicio, fim, passo):
    for i in range(inicio, fim + 1, passo):
        print(i, end=' '), sleep(0.5)

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

progressao(i, f, p)
