numeros = list()
for c in range(0,5):
    numeros.append(float(input(f'Insira um valor na posição {c}: ')))
print(numeros)
print(f'O maior numero da lista é {max(numeros)} e está na posição ', end='')
for v, num in enumerate(numeros):
    if max(numeros) == num:
        print(f'{v}...', end='')
print()
print(f'O menor numero da lista é {min(numeros)} e está na posição ', end='')
for v, num in enumerate(numeros):
    if min(numeros) == num:
        print(f'{v}...',end='')