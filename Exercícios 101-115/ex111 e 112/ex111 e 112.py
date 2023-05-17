# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.


from utilidadescev import moeda, dado

preco = dado.leiadinheirp('Informe um preço: R$')
moeda.resumo(preco,8,9)