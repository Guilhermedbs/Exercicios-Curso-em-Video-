nums =  ('zero','um','dois','três','qutro','cinco','seis' ,'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
      num = int(input('Digite um número entre 0 a 20: '))
      if  20 >= num >= 0:
            break
      print('Você inseriu um número invalido, Tente novamente!')
print(f'O número que você digitou foi o {nums[num]}')