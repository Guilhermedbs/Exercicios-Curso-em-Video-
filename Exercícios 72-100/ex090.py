# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['Nome']  = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input('Digite a média do aluno: '))
print(aluno)
if aluno['Média'] > 7:
    aluno['Situação'] = 'aprovado'
elif 5 <= aluno['Média']< 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
