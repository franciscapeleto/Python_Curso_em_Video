# mostra o maior e o menor valor digitado pelo usuario e a localizacao que foram digitados

listaNumeros = []
maior = posMaior = menor = posMenor = 0

for pos in range(0, 5):
    listaNumeros.append(int(input(f'Digite um valor para a Posicao {pos}: ')))
    if pos == 0:
        maior = menor = listaNumeros[pos]
    else:
        if listaNumeros[pos] > maior:
            maior = listaNumeros[pos]
        if listaNumeros[pos] < menor:
            menor = listaNumeros[pos]

print('=-' * 30)
print(f'Voce digitou os valores {listaNumeros}')

print(f'O maior numero digitado foi {maior} nas posicoes ', end='')
for pos, num in enumerate(listaNumeros):
    if num == maior:
        posMaior = pos
        print(f'{posMaior}...', end=' ')

print(f'\nO menor numero digitado foi {menor} nas posicoes ', end='')
for pos, num in enumerate(listaNumeros):
    if num == menor:
        posMenor = pos
        print(f'{posMenor}...', end=' ')
