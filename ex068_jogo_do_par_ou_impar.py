# jogo do par ou impar

from random import randint
print('=-'*20)
print(f'{"VAMOS JOGAR PAR OU IMPAR":^40}')
contador = 0

while True:
    print('=-' * 20)
    computador = randint(0, 9)
    jogador = int(input('Digite um numero: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Impar? [P/I] ').strip().upper()[0]
    soma = computador + jogador

    if soma % 2 == 0:
        parOuImpar = 'PAR'
    else:
        parOuImpar = 'IMPAR'

    print('-' * 40)
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma} DEU {parOuImpar}')
    print('-' * 40)

    if escolha == 'P' and parOuImpar == 'PAR':
        resultado = 'GANHOU'
    elif escolha == 'I' and parOuImpar == 'IMPAR':
        resultado = 'GANHOU'
    else:
        resultado = 'PERDEU'

    print(f'Voce {resultado}!')

    if resultado == 'PERDEU':
        break

    print('Vamos jogar novamente...')
    contador += 1

print('=-'*20)
print(f"GAME OVER! Voce venceu {contador} vez(es).")
