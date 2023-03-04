# usuario digita numeros ate ele decidir nao continuar e os numeros sao adicionados
# em tres listas: uma com todos os numeros, uma com numeros pares e uma com numeros impares

numeros = []
numerosPares = []
numerosImpares = []

while True:
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A lista completa e {numeros}')
print(f'A lista de pares e {numerosPares}')
print(f'A lista de impares e {numerosImpares}')
