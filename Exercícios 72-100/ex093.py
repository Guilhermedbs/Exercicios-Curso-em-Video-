# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
total = 0
gols = list()
jogador['nome'] = str(input('Digite o nome do jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,n):
    nums = int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}? '))
    gols.append(nums)
    total += nums
jogador['gols'] = gols[:]
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}!')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
for c in range(0,n):
    print(f'Na partida {c} fez {gols[c]} gols!')
print(f'No total foram {total} gols!')