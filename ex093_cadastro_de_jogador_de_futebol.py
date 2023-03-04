# usuario cadastra um jogador de futebol

cadastroJogador = {}
golsJogador = []
cadastroJogador['Nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {cadastroJogador["Nome"]} jogou? '))
for c in range(partidas):
    golsJogador.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
cadastroJogador['Gols'] = golsJogador[:]
cadastroJogador['Total'] = sum(golsJogador)
print('-=' * 40)
print(cadastroJogador)
print('-=' * 40)
for k, v in cadastroJogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {cadastroJogador["Nome"]} jogou {partidas} partidas.')
for c, g in enumerate(cadastroJogador['Gols']):
    print(f'{" "*4}=> Na partida {c + 1}, fez {g} gols.')
print(f"Foi um total de {cadastroJogador['Total']} gols.")