# jogo de adivinhacao

from random import randint
numeroComputador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Sera que voce consegue adivinhar qual foi?''')
numeroUsuario = ''
contador = 0
while numeroComputador != numeroUsuario:
    numeroUsuario = int(input('Qual e seu palpite? '))
    if numeroComputador > numeroUsuario:
        print('Mais... Tente mais uma vez.')
    elif numeroComputador < numeroUsuario:
        print('Menos... tente mais uma vez.')
    contador += 1

print(f'Acertou com {contador} tentativa(s). Parabens!')
