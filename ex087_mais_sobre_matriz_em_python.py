# organiza matriz

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaColuna3 = maior2 = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um numero para [{l}, {c}]: '))

print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if c == 2:
            somaColuna3 += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior2:
                maior2 = matriz[l][c]
    print()

print('-=' * 30)
print(f'A soma dos numeros pares e {somaPares}')
print(f'A soma dos numeros da terceira coluna e {somaColuna3}')
print(f'O maior valor da segunda linha e {maior2}')
