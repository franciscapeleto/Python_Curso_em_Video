# mostra a classificacao do campeonato brasileiro

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR',
         'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
         'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('=-' * 50)
print(f'Lista de times do Brasileirao 2022: {times}')
print('=-' * 50)
print(f'Os 5 primeiros sao: {times[:5]}')
print('=-' * 50)
print(f'Os 4 ultimos sao: {times[-4:]}')
print('=-' * 50)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=-' * 50)
print(f'O Fortaleza esta na {times.index("Fortaleza") + 1}ª posicao')
print('=-' * 50)
