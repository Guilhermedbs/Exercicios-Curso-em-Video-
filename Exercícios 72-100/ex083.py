# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = str(input('Digite uma expressão: '))
lista=list()
for p in exp:
    if p == '(':
        lista.append(p)
    elif p == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(p)
            break
    print(lista)
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')


