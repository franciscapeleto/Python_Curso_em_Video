# GAME: Pedra, Papel e Tesoura

from random import randint
from time import sleep

print(f''' Suas Opcoes:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
escolhaJogador = int(input(f'Qual e a sua jogada? '))
escolhaComputador = randint(1, 3)
sleep(0.3)
print(f'JO')
sleep(0.3)
print(f'KEN')
sleep(0.3)
print(f'PO!!!')
sleep(0.3)

if 1 <= escolhaJogador <= 3:
    print(f'='*30)
    if escolhaComputador == 1 and escolhaJogador == 2:
        ganhador = 'JOGADOR VENCE'
        print(f"{' Computador jogou Pedra ':=^30}\n{' Jogador jogou Papel ':=^30}")
    elif escolhaComputador == 1 and escolhaJogador == 3:
        ganhador = 'COMPUTADOR VENCE'
        print(f"{' Computador jogou Pedra ':=^30}\n{' Jogador jogou Tesoura ':=^30}")
    elif escolhaComputador == 2 and escolhaJogador == 3:
        ganhador = 'JOGADOR VENCE'
        print(f"{' Computador jogou Papel ':=^30}\n{' Jogador jogou Tesoura ':=^30}")
    elif escolhaComputador == 2 and escolhaJogador == 1:
        ganhador = 'COMPUTADOR VENCE'
        print(f"{' Computador jogou Papel ':=^30}\n{' Jogador jogou Pedra ':=^30}")
    elif escolhaComputador == 3 and escolhaJogador == 1:
        ganhador = 'JOGADOR VENCE'
        print(f"{' Computador jogou Tesoura ':=^30}\n{' Jogador jogou Pedra ':=^30}")
    elif escolhaComputador == 3 and escolhaJogador == 2:
        ganhador = 'COMPUTADOR VENCE'
        print(f"{' Computador jogou Tesoura ':=^30}\n{' Jogador jogou Papel ':=^30}")
    else:
        ganhador = 'EMPATE'
        print(f"{' EMPATE ':=^30}")
    print(f'=' * 30)
    print(ganhador)
else:
    print(f'OPCAO INVALIDA! Escolha um numero de 1 a 3. Tente Novamente!')
