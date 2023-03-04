# mostra a quantidade de termos da sequencia de fibonacci escolhida pelo usuario

print('=' * 40)
print(f'{"Sequencia de Fibonacci":^40}')
print('=' * 40)
termo = int(input('Quantos termos voce quer mostrar? '))
print('~' * 40)
contador = 2
primeiroFibonacci = 0
segundoFibonacci = 1
print(f'{primeiroFibonacci} → {segundoFibonacci} → ', end='')

while contador < termo:
    proximoFibonacci = primeiroFibonacci + segundoFibonacci
    print(f'{proximoFibonacci:,} → ', end='')
    primeiroFibonacci = segundoFibonacci
    segundoFibonacci = proximoFibonacci
    contador += 1
print('FIM')
print('~' * 40)
