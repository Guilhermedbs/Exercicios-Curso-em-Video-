def moeda(num,moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')


def dobro(num, format = False):
    d = num * 2
    if format:
        return moeda(d)
    else:
        return d

def metade(num,format = False):
    m = num / 2
    if format:
        return moeda(m)
    else:
        return m

def aumentar(num,porcen = 10,format = False):
    maior = num*(1 + (porcen/100))
    if format:
        return moeda(maior)
    else:
        return maior


def diminuir(num,porcen = 1, format = False):
    menor = num*(1 - (porcen/100))
    if format:
        return moeda(menor)
    else:
        return menor

