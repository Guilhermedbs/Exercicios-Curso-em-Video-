# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
gols = list()
time = []
while True:
    jogador.clear()
    gols.clear()
    total = 0
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0,n):
        nums = int(input(f'Quantos gols {jogador["nome"]} fez na partida {c+1}? '))
        gols.append(nums)
        total += nums
    jogador['gols'] = gols[:]
    jogador['total'] = total
    print('-='*30)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Valor invalido, digite apenas S ou N!')
    if resp == 'N':
            break
print(time)
print(f'{"Num":<5}{"Nome":<12} {"Gols":<15} {"Total":<8}')
print('-='*30)
for c in range(0,len(time)):
    print(f'{str(c):<5}{str(time[c]["nome"]):<12} {str(time[c]["gols"]):<15} {str(time[c]["total"]):<8}')
print('-='*30)
while True:
    n = int(input('Mostrar o levamento de qual jogador?(999 para parar) '))
    if n == 999:
        break
    elif n > (len(time)-1) or n < 0:
        print('Valor invalido, Tente novamente!')
    else:
        print(f'O jogador {time[n]["nome"]} jogou {len(time[n]["gols"])} partidas.')
        for c in range(0,len(time[n]['gols'])):
            print(f'Na partida {c+1} fez {time[n]["gols"][c]} gols!')
        print(f'No total foram {time[n]["total"]} gols!')