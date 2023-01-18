# imprime o número o dobro, o triplo e a raiz quadrada do número digitado

n = int(input('Digite um número: '))
print('O dobro de {} é {}.'.format(n, n * 2))
print('O triplo de {} é {}.'.format(n, n * 3))
print('A raiz de quadrada de {} é {:.5f}.'.format(n, n ** (1/2)))
