# estatisticas em produtos

print('-' * 40)
print(f'{"LOJA TEM TUDO":^40}')
print('-' * 40)
totalCompras = contadorMaior1000 = contador = 0
precoMaisBarato = ''

while True:
    continuar = ' '
    nomeProduto = input('Nome do Produto: ')
    precoProduto = float(input('Preco: R$'))
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    totalCompras += precoProduto
    contador += 1
    if precoProduto > 1000:
        contadorMaior1000 += 1
    if contador == 1 or precoProduto < precoMaisBarato:
        produtoMaisBarato = nomeProduto
        precoMaisBarato = precoProduto
    if continuar == 'N':
        break

print(f'{" FIM DO PROGRAMA ":-^40}')
print(f"O total da compra foi R${totalCompras:,.2f}")
print(f'Temos {contadorMaior1000} produto(s) custando mais de R$1,000.00')
print(f'O produto mais barato foi {produtoMaisBarato} que custa R${precoMaisBarato:,.2f}')
