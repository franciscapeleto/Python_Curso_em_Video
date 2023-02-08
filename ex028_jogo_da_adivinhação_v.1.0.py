# Jogo de Adivinhação

from random import randint
from time import sleep
título = '\33[34mVou pensar em um número entra 0 e 5. Tente adivinhar...'
print('\33[33m-=-'*20+'\33[m')
print('{:^65}'.format(título))
print('\33[33m-=-'*20+'\33[m')
numero = int(input('Em que numero eu pensei? '))
sorteio = randint(0,5)
print('\33[35mPROCESSANDO...\33[m')
sleep(3)

if numero == sorteio:
    print('\33[32mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\33[31mGANHEI! Eu pensei no número {} e não no {}'.format(sorteio, numero))
