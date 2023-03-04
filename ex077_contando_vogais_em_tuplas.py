# contador de vogais

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for vogal in palavra:
        if vogal in 'aeiou':
            print(vogal, end=' ')
