# mostra a progressao aritmetica escolhida pelo usuario

print('=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('=' * 30)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))

for c in range(primeiroTermo, primeiroTermo + (10 * razao), razao):
    print(c, end=' → ')
print(f'ACABOU')
