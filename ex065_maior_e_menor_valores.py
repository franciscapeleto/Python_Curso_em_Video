# usuario digita quantos numeros quiser e o programa calcula a media entre eles
# e mostra o maior e o menor valor

soma = contador = maior = menor = 0
sair = ''

while sair != 'N':
    numero = int(input('Digite um numero: '))
    sair = input('Quer continuar? [S/N] ').strip().upper()[0]
    if contador == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    soma += numero
    contador += 1

media = soma / contador
print(f'Voce digitou {contador} numeros e a media foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
