# analisa se uma frase e palindromo

frase = input('Digite uma frase: ').strip().upper()
fraseJunto = ''
for c in frase:
    if c != ' ':
        fraseJunto += c
fraseJuntoInvertida = fraseJunto[::-1]
print(f'O inverso de {fraseJunto} e {fraseJuntoInvertida}')

if fraseJunto == fraseJuntoInvertida:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')
