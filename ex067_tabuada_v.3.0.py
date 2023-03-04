# imprime a tabuada do número digitado

while True:
    número = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if número < 0:
        break
    for c in range(1, 11):
        print('{} x {:2} = {:4}'.format(número, c, número * c))
    print('-' * 40)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
