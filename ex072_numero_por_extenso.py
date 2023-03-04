# mostra o numero que o usuario escolher por extenso

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o numero {numeros[escolha]}')
