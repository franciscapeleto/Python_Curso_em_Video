# usuario cadastra um jogador de futebol

time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do Jogador: ')
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Digite apenas "S" ou "N"')
    if resp in 'N':
        break

print('-=' * 25)
print(f'{"COD":<5}{"NOME":<15}{"GOLS":<25}{"TOTAL":<5}')
print('-' * 50)
for c, l in enumerate(time):
    print('{:>3}  {:<15}{:<25}{:>5}'.format(c, l['Nome'], str(l['Gols']), str(l['Total'])))
print('-' * 50)

while True:
    contador = 1
    while True:
        busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if 0 <= busca < len(time):
            print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
            break
        elif busca == 999:
            break
        else:
            print(f'ERRO! Nao existe jogador com codigo {busca}')
            print(f'Digitar um numero >= 0 e < {len(time)}')
            print('-' * 50)
    if busca == 999:
        print('-' * 50)
        break
    for j in time[busca]['Gols']:
        print(f'\tNo jogo {contador} fez {j}.')
        contador += 1
    print('-' * 50)

print('<< VOLTE SEMPRE >>')
