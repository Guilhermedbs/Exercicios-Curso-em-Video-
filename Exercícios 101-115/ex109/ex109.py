# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda
preco = float(input('Digite um preço R$'))
print( f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco)}')
print( f'A metade de {moeda.moeda(preco)} é R${moeda.metade(preco)}')
print (f'Aumentando {moeda.moeda(preco)} em 10% se obtem {moeda.aumentar(preco)}!')
print( f'Diminuindo {moeda.moeda(preco)} em 10% se obtem {moeda.diminuir(preco)}!')