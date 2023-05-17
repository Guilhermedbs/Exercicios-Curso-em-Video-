num1 = int(input('Insira um número:'))
num2 = int(input('Insira outro número:'))
num3 = int(input('Insira outro número:'))
num4 = int(input('Insira outro número:'))
numeros = (num1 , num2, num3, num4)
print(f'Você digitou os valores: {numeros}')
if 9 in numeros:
    print(f'O número nove apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 aparece na {numeros.index(3)+1}° posição')
print( 'Os valores pares entre os valores digitados são ', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')