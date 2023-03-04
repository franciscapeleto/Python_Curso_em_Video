# mostra o maior valor de numeros aleatorios

def leiaInt(numero):
    print('-' * 40)
    while True:
        nInt = input(numero)
        if nInt.isnumeric():
            nInt = int(nInt)
            break
        else:
            print('\33[31mERRO! Digite um numero inteiro valido.\33[m')
    return nInt


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
