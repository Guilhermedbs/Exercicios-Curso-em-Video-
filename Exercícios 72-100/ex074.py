from random import randint
maior = menor = c = 0
nums = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os números sorteados foram: {nums}')
for num in nums:
    if c == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    c += 1
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')
