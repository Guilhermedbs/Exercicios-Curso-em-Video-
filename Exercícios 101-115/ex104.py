# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(frase):
    

    print(frase, end=' ')
    num = str(input())
    while num.isnumeric() == False:
          print('Valor invalido, tente novamente!')
          print(frase, end=' ')
          num = str(input())
    return int(num)


n = leiaint('Digite um número:')
print(f'O valor que você digtou foi {n}')