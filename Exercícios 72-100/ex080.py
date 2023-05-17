#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
nums = list()
pos = 0
for c in range(0,5):
    n = int(input('Insira um valor: '))
    if c == 0 or n > max(nums):
        nums.append(n)
        print('Valor adcionado ao final da lista')
    else:
        while pos < (len(nums)):
            if n <= nums[pos]:
                nums.insert(pos,n)
                print(f'O valor foi adcionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados foram: {nums}')
