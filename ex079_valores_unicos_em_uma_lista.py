# usuario digita numeros ate ele decidir nao continuar e os numeros sao adicionados
# em uma lista sem repetir e em ordem crescente

numeros = []
while True:
    numero = int(input('Digite um numero: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

numeros.sort()
print('-=' * 20)
print(f'Voce digitou os valores {numeros}')
