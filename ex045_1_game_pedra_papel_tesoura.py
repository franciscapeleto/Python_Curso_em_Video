# GAME: Pedra, Papel e Tesoura

from random import randint
from time import sleep

escolhasPossiveis = ('Pedra', 'Papel', 'Tesoura')
print(f''' Suas Opcoes:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input(f'Qual e a sua jogada? '))
computador = randint(1, 3)
try:
    escolhaJogador = escolhasPossiveis[jogador - 1]
    escolhaComputador = escolhasPossiveis[computador - 1]
    sleep(0.5)
    print(f'JO')
    sleep(0.5)
    print(f'KEN')
    sleep(0.5)
    print(f'PO!!!')
    sleep(0.5)
    print(f'='*30)
    print(f"{f' Computador jogou {escolhaComputador} ':=^30}\n{f' Jogador jogou {escolhaJogador} ':=^30}")
    print(f'='*30)
    if 1 <= jogador <= 3:
        if computador == 1 and jogador == 2:
            ganhador = 'JOGADOR'
        elif computador == 1 and jogador == 3:
            ganhador = 'COMPUTADOR'
        elif computador == 2 and jogador == 3:
            ganhador = 'JOGADOR'
        elif computador == 2 and jogador == 1:
            ganhador = 'COMPUTADOR'
        elif computador == 3 and jogador == 1:
            ganhador = 'JOGADOR'
        elif computador == 3 and jogador == 2:
            ganhador = 'COMPUTADOR'
        else:
            ganhador = 'NINGUEM'
    print(f'{ganhador} VENCE')
except:
    print(f'OPCAO INVALIDA! Escolha um numero de 1 a 3. Tente Novamente!')
