# palpites para a mega sena

from random import randint
from time import sleep
print('-=' * 20)
print(f'{"JOGAR NA MEGA SENA":^40}')
print('-=' * 20)
nApostas = int(input('Quantos jogos voce quer que eu sorteie? '))
nCadaJogo = []
nTotalJogos = []

for n in range(nApostas):
    contador = 0
    while contador < 6:
        numero = randint(1, 60)
        if numero not in nCadaJogo:
            nCadaJogo.append(numero)
        contador += 1
    nCadaJogo.sort()
    nTotalJogos.append(nCadaJogo[:])
    nCadaJogo.clear()
print('-=' * 20)
print(f'{f" SORTEANDO {nApostas} JOGOS ":-^40}')
for c, j in enumerate(nTotalJogos):
    print(f'Jogo {c+1}: {j}')
    sleep(1)
print(f'{" < BOA SORTE! > ":-^40}')
