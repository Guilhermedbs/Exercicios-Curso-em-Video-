# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
valores =[[] , []]
for c in range(0,7):
    valor = int(input('Digite um valor:'))
    if valor%2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
if len(valores[0]) > 0:
    print(f'Os valores pares digitados foram: {valores[0]}')
if len(valores[1]) > 0:
    print(f'Os valores impares digitados foram: {valores[1]}')