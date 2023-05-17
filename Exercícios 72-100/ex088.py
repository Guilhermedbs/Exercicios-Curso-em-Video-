# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
jogo = list()
jogos = list()
quant = int(input('Digite a quantidade de jogos: '))
for l in range(0,quant):
    jogo.clear()
    for c in range(0,6):
        valor = randint(1,60)
        jogo.append(valor)
    jogo.sort()
    jogos.append(jogo[:])
for c in range(0,quant):
    print(f'jogo [ {c+1} ]: {jogos[c]}')
