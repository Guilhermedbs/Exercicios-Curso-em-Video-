# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[],[],[]]
for c in range(0,3):
    for p in range(0,3):
        valor = int(input(f'Digite o valor para a posição {(c+1,p+1)}: '))
        matriz[c].append(valor)
for c in range(0,3):
    for p in range(0,3):
            print(f'[ {matriz[c][p]:^5} ]',end='')
    print()
