# usuario digita quantos numeros quiser e o programa soma todos eles

soma = numero = contador = 0

while numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero != 999:
        soma += numero
        contador += 1

print(f'Voce digitou {contador} numeros e a soma entre eles foi {soma}')
