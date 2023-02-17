# imprime a tabuada do número digitado

número = int(input('Digite um número para saber a tabuada dele: '))

for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(número, c, número * c))
