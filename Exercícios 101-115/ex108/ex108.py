# Exercício Python 108: Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import moeda
preco = float(input('Digite um preço R$'))
print( f'O dobro de {moeda.moeda(preco)} é R${moeda.moeda(moeda.dobro(preco))}')
print( f'A metade de {moeda.moeda(preco)} é R${moeda.moeda(moeda.metade(preco))}')
print (f'Aumentando {moeda.moeda(preco)} em 10% se obtem R${moeda.moeda(moeda.aumentar(preco))}!')
print( f'Diminuindo {moeda.moeda(preco)} em 10% se obtem R${moeda.moeda(moeda.diminuir(preco))}!')