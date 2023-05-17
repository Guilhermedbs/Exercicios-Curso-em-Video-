# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições
def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade > 18:
        situação = 'Obrigatório votar'
    elif 18 > idade >= 16:
        situação = 'Opcional votar'
    else:
        situação = 'Não vota'
    return f'Com {idade} anos: {situação}'


nas = int(input('Em que ano você nasceu? '))
print(voto(nas))
