# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    n = len(msg) + 4
    print('~'*n)
    print(f'  {msg}')
    print('~'*n)


texto = str(input(('Digite algo: ')))
escreva(texto)