# mostra o maior valor de numeros aleatorios

def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    maior = 0
    for n in num:
        print(n, end=' ')
        if n > maior:
            maior = n
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
