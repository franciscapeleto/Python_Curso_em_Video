# organiza matriz

matriz = [[], [], []]
numero = 0

for p in range(3):
    for s in range(3):
        numero = int(input(f'Digite um numero para [{p}, {s}]: '))
        matriz[p].append(numero)

print('-=' * 30)
for mat in matriz:
    for c, m in enumerate(mat):
        if (c + 1) % 3 == 0:
            print(f'[{m:^4}]')
        else:
            print(f'[{m:^4}]', end=' ')
