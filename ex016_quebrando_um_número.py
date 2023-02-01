# mostra a porção inteiro de um número decimal que o usuário escolher

from math import trunc
numFloat = float(input('Digite um número em decimal: '))
print('O número digitado foi {} e a sua porção inteira é {}'.format(numFloat, trunc(numFloat)))
