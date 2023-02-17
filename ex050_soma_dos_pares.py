# soma os numeros pares que foram digitados

somaPares = 0
contadorPares = 0

for c in range(1, 7):
    número = int(input(f'Digite o {c}° número inteiro: '))
    if número % 2 == 0:
        somaPares += número
        contadorPares += 1

print(f'A soma de {contadorPares} numero(s) PAR(ES) digitado(s) foi de {somaPares}')
