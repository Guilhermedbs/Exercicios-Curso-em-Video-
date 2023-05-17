# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoas = list()
pessoa = {}
mulheres = []
velhas = []
total = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome da pessoa: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Digite o sexo da pessoa[M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('Valor invalido, digite apenas M ou F!')
        else:
            break
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    pessoas.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
    total += pessoa['idade']
    while True:
        resp = str(input('Quer continuar?[S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        else:
            print('Valor invalido, digite apenas S ou N!')
    if resp == 'n':
        break
media = total/len(pessoas)
print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas e a média de idade das pessoas foram {media} anos!')
print('-='*30)
if len(mulheres) > 0:
    print(f'As mulheres são: {mulheres}')
    print('-=' * 30)
for c in range(0,len(pessoas)):
    if pessoas[c]['idade'] > media:
        velhas.append(pessoas[c].copy())
print(f'As pessoas com a idade acima da media: {velhas}')
