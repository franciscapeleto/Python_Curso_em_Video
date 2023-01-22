# imprime o valor em dólares do valor digitado em reais

reais = float(input('Quantos reais você tem na carteira? R$'))
print('Com R${:,.2f} você pode comprar US${:,.2f}'.format(reais, reais / 5.27))
