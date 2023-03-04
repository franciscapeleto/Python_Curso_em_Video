# usuario digita cinco numeros e o programa mostra
# em qual posicao o numero foi adicionado em uma lista

numeros = []
for p in range(0, 5):
    numero = int(input('Digite um numero: '))
    if p == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if numero < numeros[pos]:
                numeros.insert(pos, numero)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1

print('-=' * 20)
print(f'Voce digitou os valores {numeros}')
