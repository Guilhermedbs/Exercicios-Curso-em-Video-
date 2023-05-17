# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.
from datetime import date
ano = date.today().year
Dados = dict()
Dados['nome'] = str(input('Nome: '))
Dados['idade'] =(ano - int(input('Ano de nascimento: ')))
Dados['ctps'] = int(input('Número de carteira de trabalho(0 não tem!): '))
if Dados['ctps'] > 0:
    Dados['contratação'] = int(input('Ano de Contratação: '))
    Dados['salário'] = float(input('Valor do salário: '))
    Dados['aposentadoria'] = (Dados['idade'] + (Dados['contratação'] +35)- ano)
for k, v in Dados.items():
    print(f'{k} tem o valor {v}')
