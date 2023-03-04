# usuario digita quantos numeros quiser e o programa soma todos eles

soma = contador = 0

while True:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'Voce digitou {contador} numeros e a soma entre eles foi {soma}')
