palavras=('Aprender','Programar','Linguagem','Python','Curso','Gratis',)
for palavra in palavras:
    print(f'\nAs vogais presentes em {palavra} são: ', end='')
    for c in range(0,len(palavra)):
        if palavra[c].lower() in 'aeiou':
            print(f'{palavra[c]} ', end='')

