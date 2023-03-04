# sorteia cinco numero e soma os numero pares

from random import randint

def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for l in range(5):
        numeros.append(randint(1, 10))
        print(numeros[l], end=' ')
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia()
somaPar(numeros)
