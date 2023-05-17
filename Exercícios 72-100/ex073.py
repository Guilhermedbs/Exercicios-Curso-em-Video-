times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR',
         'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo','Santos', 'Goiás',
         'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO' ,'Avaí', 'Juventude')
c = 0
print (f'Lista de times do Brasileirão: {times}')
print (f'Os primeiros 5 colocados são {times[0:5]}')
print (f'Os ultimos 4 colocados são {times[-4:]}')
print(f"O Fortaleza está na {times.index('Fortaleza')+1}° posição")
print(f'A lista dos times em ordem alfabética é {sorted(times)}')
