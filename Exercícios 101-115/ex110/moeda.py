def moeda(num,moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')


def dobro(num, format = True):
    d = num * 2
    if format:
        return moeda(d)
    else:
        return d

def metade(num,format = True):
    m = num / 2
    if format:
        return moeda(m)
    else:
        return m

def aumentar(num,porcen = 10,format = True):
    maior = num*(1 + (porcen/100))
    if format:
        return moeda(maior)
    else:
        return maior


def diminuir(num,porcen = 1, format = True):
    menor = num*(1 - (porcen/100))
    if format:
        return moeda(menor)
    else:
        return menor

def resumo(num, a, d):
    print('-'*33)
    print(f'{"         RESUMO DO VALOR"}')
    print('-'*33)
    print(f'{"Preço analizado:":<20}{moeda(num):<20}')
    print(f'{"O dobro do preço:":<20}{dobro(num):<20}')
    print(f'{"Metade do preço:":<20}{metade(num):<20}')
    print(f'{a}{"% de aumento:":<19}{aumentar(num,a):<20}')
    print(f'{d}{"% de redução:":<19}{diminuir(num,d):<20}')
