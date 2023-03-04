# usuario digita numeros ate ele decidir nao continuar e os numeros sao adicionados
# em uma lista ordem decrescente, mostra o total de numeros digitados e se o numero 5 esta na lista

numeros = []

while True:
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

numeros.sort(reverse=True)
print('-=' * 30)
print(f'Voce digitou {len(numeros)} numeros.')
print(f'Os numeros em ordem decrescente sao {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')
