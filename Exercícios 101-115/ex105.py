# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
def notas(*num,sit = False):
    """
    ->Função que recebe a nota de vários alunos e retorna um dicionário com varias informações da turma
    :param num: notas que a turma tirou.
    :param sit: se deseja ou não saber a situlção da turma usando sit = True.
    :return: média, maior nota, menor nota, total de notas e a situação da turma(opcional).
    """
    turma = dict()
    total = maior = menor = soma = 0
    for nota in num:
            if total == 0:
                maior = menor = nota
            else:
                if nota > maior:
                    maior = nota
                if nota < menor:
                    menor = nota
            soma += nota
            total += 1
            media = soma/total
    turma['total'] = total
    turma['media'] = media
    turma['maior'] = maior
    turma['menor'] = menor
    if sit:
        if media > 7:
            turma['situação'] = 'Boa'
        elif 7 > media > 5:
            turma['situação'] = 'Razoavel'
        else:
            turma['situação'] = 'Ruim'
    return turma
print(notas(2,10,9,8,3))