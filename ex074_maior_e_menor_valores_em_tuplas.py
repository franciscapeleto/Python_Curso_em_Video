# sorteia 5 numeros e mostra o maior e o menor

from random import randint
numero = (randint(1, 9), randint(1, 9), randint(1, 9),
          randint(1, 9), randint(1, 9))
print('Os numeros sorteados foram: ', end='')
for n in numero:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')
