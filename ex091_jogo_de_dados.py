# jogo de dados

from random import randint
from operator import itemgetter
jogadas = {}
ranking = {}

for j in range(1, 5):
    jogadas[f'Jogador {j}'] = randint(1, 6)

print('Valores sorteados:')

for k, v in jogadas.items():
    print(f'\33[34m{k}\33[m tirou \33[31m{v}\33[m no dado.')

print('-=' * 20)
print(f'{" RANKING DOS JOGADORES ":=^40}')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for c, r in enumerate(ranking):
    print("{}\33[32m{}º\33[m lugar: \33[34m{} \33[mcom \33[31m{}".format(' ' * 7, c + 1, r[0], r[1]))
