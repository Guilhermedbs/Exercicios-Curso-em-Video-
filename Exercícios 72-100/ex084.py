# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
count = 0
pessoas = list()
pesado = list()
leve = list()
dados = list()
maior = menor = 0
print('Insira o nome e o peso de quantas pessoas desejar!')
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados)
    if count == 0:
        maior = dados[1]
        menor = dados[1]
        pesado.append(dados[:])
        leve.append(dados[:])
    elif dados[1] > maior:
        pesado.clear()
        pesado.append(dados[:])
        maior = dados[1]
    elif dados[1] < menor:
        leve.clear()
        leve.append(dados[:])
        menor = dados[1]
    elif dados[1] == maior:
        pesado.append(dados[:])
    elif dados[1] == menor:
        leve.append(dados[:])
    count += 1
    resp = str(input('Deseja continuar[S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
    dados.clear()
print(f'No total foram cadastradas {count} pessoas!')
print(f'O maior peso foi {maior } Kg, Peso de ', end='')
for p in pesado:
    if p == pesado[-1]:
        print(p[0])
    else:
         print(p[0], end=' e ')

print(f'O menor peso foi {menor} Kg, Peso de ', end='')
for p in leve:
    if p == leve[-1]:
         print(p[0])
    else:
        print(p[0], end=' e ')
