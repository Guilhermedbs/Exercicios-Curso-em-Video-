# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[],[],[]]
soma = 0
soma3 = 0
maior = 0
for c in range(0,3):
    for p in range(0,3):
        valor = int(input(f'Digite o valor para a posição {(c+1,p+1)}: '))
        matriz[c].append(valor)
        if valor%2 == 0:
            soma += valor
        if p == 2:
            soma3 += valor
        if c == 1:
            if p == 0:
                maior = valor
            elif valor > maior:
                    maior = valor
for c in range(0,3):
    for p in range(0,3):
            print(f'[ {matriz[c][p]:^5} ]',end='')
    print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}.')