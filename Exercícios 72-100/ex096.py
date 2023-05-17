# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(x,y):
    a = x*y
    print(f'A área do terreno de {x}x{y} é de {a} metros quadrados!')


l = float(input('Qual a largura do terreno(m)? '))
c = float(input('Qual o comprimento do terreno(m)? '))
área(l,c)