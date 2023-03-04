# usuario cadastra sete numero onde o programa separa
# os pares e impares em duas listas dentro de uma lista

lista = [[], []]
numero = 0

for c in range(1, 8):
    numero = int(input(f'Digite o {c}º numero: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()
print('-=' * 40)
print(f'Os numeros pares digitados foram: {lista[0]}')
print(f'Os numeros impares digitados foram: {lista[1]}')
