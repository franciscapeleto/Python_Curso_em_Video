# usuario digita cinco numeros e o programa mostra
# em qual posicao o numero foi adicionado em uma lista

numeros = []
for p in range(0, 5):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    numeros.sort()
    local = numeros.index(numero)
    if local == (len(numeros)) - 1:
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posicao {local} da lista...')

print('-=' * 20)
print(f'Voce digitou os valores {numeros}')
