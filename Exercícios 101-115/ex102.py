# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show = False):
    """
    Calcula o fatorial de um número!
    :param num: número do qual quer o fatorial
    :param show:(opcional) escolhe se mostra ou não o calculo feito para atingir o fatorial
    :return:retorna o valor final do fatorial
    """
    c = num
    fator = 1
    while c >= 1:
        if show:
            print(f'{c} ',end='')
            if c > 1:
                print('x ',end='')
            else:
                print('= ', end='')
        fator *= c
        c -= 1
    return fator


print(fatorial(10,True))
help(fatorial)