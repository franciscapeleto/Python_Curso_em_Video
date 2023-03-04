# mostra a progressao aritmetica escolhida pelo usuario

print('=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('=' * 30)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
c = 0

while c < 10:
    print(primeiroTermo, end=' → ')
    primeiroTermo += razao
    c += 1

print(f'FIM')
