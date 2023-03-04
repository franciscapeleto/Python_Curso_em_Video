# mostra a progressao aritmetica escolhida pelo usuario

print('=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('=' * 30)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = 10
contador = 0
contadorTermo = 0

while termo != 0:
    while contador < termo:
        print(primeiroTermo, end=' → ')
        primeiroTermo += razao
        contador += 1
        contadorTermo += 1
    print(f'PAUSA')
    termo = int(input('quantos termos voce quer mostrar a mais? '))
    contador = 0

print(f'Progressao finalizada com {contadorTermo} termos mostrados.')
