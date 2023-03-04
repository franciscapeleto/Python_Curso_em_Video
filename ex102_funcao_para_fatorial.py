# mostra o maior valor de numeros aleatorios

def fatorial(numero, show):
    '''
    -> Calcula o Fatorial de um numero.
    :param numero: O numero a ser calculado
    :param show: Mostrar ou nao a operacao
    :return: O valor do Fatorial de um numero
    '''
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    if show:
        for c in range(numero, 0, -1):
            if c > 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
        return f
    else:
        return f


print('-' * 40)
qualFatorial = int(input('Quer saber o fatorial de qual numero? '))

while True:
    showSN = input('Quer ver a operacao completa? [S/N] ').strip().upper()[0]
    if showSN == 'S':
        showSN = True
        break
    elif showSN == 'N':
        showSN = False
        break
    else:
        print('ERRO! Digite apenas S ou N!')

print(fatorial(qualFatorial, showSN))
