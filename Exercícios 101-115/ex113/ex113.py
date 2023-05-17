def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('Erro! Por favor digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário!')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('Erro! Por favor digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário!')
            return 0
        else:
            return n



num = leiaint('Digite um número inteiro: ')
print(f'O número digitado foi {num}')
num2 = leiafloat('Digite um número real: ')
print(f'O número digitado foi {num2}')