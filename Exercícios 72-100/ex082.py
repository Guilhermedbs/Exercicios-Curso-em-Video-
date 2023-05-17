# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Insira um valor: '))
    lista.append(n)
    resp = str(input('Deseja continuar?[S/N]')).strip()
    if resp in 'Nn':
        break
for c in range(0,len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
lista.sort()
pares.sort()
impares.sort()
print(f'A lista completa é :{lista}')
print(f'OS valores que são pares da lista são: {pares}')
print(f'OS valores que são impares da lista são: {impares}')