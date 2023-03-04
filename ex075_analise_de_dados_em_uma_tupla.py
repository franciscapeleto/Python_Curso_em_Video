# analisa dados em uma tupla

todos = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {todos}')
print(f'O valor 9 apareceu {todos.count(9)} vez(es)')
if 3 in todos:
    print(f'O valor 3 apareceu na {todos.index(3) + 1}ª posicao')
else:
    print('O valor 3 nao foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for n in todos:
    if n % 2 == 0:
        print(n, end=' ')