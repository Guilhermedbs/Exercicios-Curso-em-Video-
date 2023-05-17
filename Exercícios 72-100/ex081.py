# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
while True:
    n = int(input('Insira um valor: '))
    lista.append(n)
    resp = str(input('Deseja continuar?[S/N]')).strip()
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'A) A lista em ordem decrescente é {lista}')
print(f'B) A quantidade de valores que foram digitados foi {len(lista)}!')
if 5 in lista:
    print('C) O o valor 5 foi inserido e está na lista')
else:
    print('C) O o valor 5 não foi inserido e não está na lista')
