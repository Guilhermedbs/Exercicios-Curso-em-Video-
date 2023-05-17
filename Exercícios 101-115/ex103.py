# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador, gols):
    if len(jogador) == 0:
         jogador = '<desconhecido>'
         if gols.isnumeric():
            gols = int(gols)
         else:
            gols = 0
    return f'o jogador {jogador} fez {gols} gols!'

nome = str(input('Qual o nome do jogador?'))
qnt = str(input('Quantos gols o jogador fez? '))
print(ficha(nome,qnt))