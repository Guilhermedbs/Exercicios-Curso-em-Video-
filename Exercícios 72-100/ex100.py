# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando valores da lista: ', end='')
    for c in range(0,5):
        num = randint(1,10)
        print(f'{num} ', end ='')
        lista.append(num)
    print('Pronto!')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor%2 == 0:
            soma += int(valor)
    print(f'Somando os valores pares {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)