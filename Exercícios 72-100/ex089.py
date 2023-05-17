# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
lista = list()
alunos = list()
resp = 's'
while resp not in 'Nn':
    alunos.clear()
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos.append(nome)
    alunos.append(n1)
    alunos.append(n2)
    lista.append(alunos[:])
    resp = str(input('Deseja continuar?[S/N]')).strip()[0]
print(lista)

for c in range(0,len(lista)):
    print(f'No: {c}  NOME: {lista[c][0]}  MEDIA: {(lista[c][1]+lista[c][2])/2}')
while True:
    n = int(input('Digite o número do aluno que você deseja ver individualmente (Digite 999 para parar): '))
    if n == 999:
        break
    elif n > len(lista):
        print('não há esse aluno no boletim. Tente novamente!')
    else:
        print(f'Aluno: {lista[n][0]} /  NOTA 1: {lista[n][1]} / NOTA 2: {lista[n][2]}')


