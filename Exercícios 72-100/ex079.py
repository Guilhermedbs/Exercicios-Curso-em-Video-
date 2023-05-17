#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list()
while True:
    num = (int(input('Insira um valor:')))
    if num in valores:
        print('O valor já existe na lista e não sera adicionado novamente')
    else:
        valores.append(num)
        print('O valor foi adicionada a lista!')
    resp = str(input('Você deseja continuar?[S/N) ')).strip().upper()
    if 'N' in resp:
        break
valores.sort()
print(f'Os valores que você inseriu foram: {valores}')