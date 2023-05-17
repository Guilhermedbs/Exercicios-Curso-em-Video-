# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    total = maior = 0
    for valor in num:
        print(f'{valor} ',end='')
        if total == 0:
            maior = valor
        else:
            if maior < valor:
                maior = valor
        total += 1
    print(f'Foram inseridos {total} valores ao todo!')
    print(f'E o maior é {maior}')



maior(2, 3, 4, 6,20,15,14)
maior()