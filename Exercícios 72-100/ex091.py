# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
from time import sleep
c = 1
ordem = list
jogo = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 'jogador3':randint(1,6), 'jogador4':randint(1,6)}
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ordem = sorted(jogo.items(), key=itemgetter(1), reverse = True)
for k, v in ordem:
    print(f'O {k} ficou em {c}° lugar com {v} no dado!')
    sleep(1)
    c += 1