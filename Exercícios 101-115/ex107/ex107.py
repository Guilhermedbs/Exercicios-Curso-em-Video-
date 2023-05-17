# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
preco = float(input('Digite um preço: '))
print( f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print( f'A metade de R${preco} é R${moeda.metade(preco)}')
print (f'Aumentando R${preco} em 10% se obtem R${moeda.aumentar(preco)}!')
print( f'Diminuindo R${preco} em 10% se obtem R${moeda.diminuir(preco)}!')