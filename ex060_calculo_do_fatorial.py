# calcula o fatorial de um numero

produto = 1
numero = int(input('Digite um numero para\ncalcular seu Fatorial: '))

while numero > 0:
    print(f'Calculando {numero}! = ', end= '')
    for f in range(numero, 0, -1):
        produto *= numero
        if numero > 1:
            print(f'{f}', end= ' x ')
        else:
            print(f'{f} = {produto:,}')
        numero -= 1
