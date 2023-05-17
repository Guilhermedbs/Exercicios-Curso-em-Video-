# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. S
# eu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
def contador(i, f, p):
    while p <= 0:
        print('Erro, valor do passo não pode ser negativo ou nulo!')
        p = int(input('Insira o passo novamente: '))
    c = i
    print('=-='*20)
    print(f'Contagem de {i} a {f} de {p} em {p}')
    while True:
        print(f'{c} ',end='')
        if f > i:
            c += p
            if c > f:
                break
        else:
            c -= p
            if c < f:
                break
    print('Fim!')
    print('=-=' * 20)


contador(1,10,1)
contador(10,0,2)
print('Agora personalize a sua própria contagem!')
inicio = int(input('Inicio: '))
final = int(input('final: '))
passo = int(input('passo: '))
contador(inicio,final,passo)