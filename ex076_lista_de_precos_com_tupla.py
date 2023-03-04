# lista de precos com tupla

listagem = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 50)
print(f"{'LISTAGEM DE PRECOS':^50}")
print('-' * 50)

for l in range(0, len(listagem)):
    if l % 2 == 0:
        print(f'{listagem[l]:.<40}', end='')
    else:
        print(f'R${listagem[l]:>8.2f}')

print('-' * 50)
