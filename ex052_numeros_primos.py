# mostra a quantidade de vezes que um numero e divisivel e se ele e primo

numero = int(input('Primeiro termo: '))
contador = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\33[33m{c}', end=' ')
        contador += 1
    else:
        print(f'\33[31m{c}', end=' ')

if contador != 2:
    primo = 'NAO E PRIMO'
else:
    primo = 'E PRIMO'

print(f'\n\33[mO numero {numero} foi divisivel {contador} vez(es)')
print(f'E por isso ele {primo}!')
