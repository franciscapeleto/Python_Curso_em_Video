# Formas de pagamento
titulo = ' LOJAS CAPELETO '
print('='*30)
print('{:=^30}'.format(titulo))
print('='*30)
valorCompra = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcaoCompra = int(input('Qual e a opcao? '))

if opcaoCompra == 1:
    totalCompra = valorCompra * 0.9
elif opcaoCompra == 2:
    totalCompra = valorCompra * 0.95
elif opcaoCompra == 3:
    totalCompra = valorCompra
    valorParcelas = valorCompra / 2
    print(f'Sua compra sera parcelada em 2x de R${valorParcelas:,.2f} SEM JUROS')
elif opcaoCompra == 4:
    totalCompra = valorCompra * 1.2
    parcelas = int(input('Quantas parcelas? '))
    if parcelas < 3:
        totalCompra = 0
        print(f'Nao e possivel calcular parcelas menores que 3x! Tente novamente!')
    else:
        parceladoCartao = totalCompra / parcelas
        print(f'Sua compra sera parcelada em {parcelas}x de R${parceladoCartao:,.2f} COM JUROS')
else:
    totalCompra = 0
    print(f'OPCAO INVALIDA DE PAGAMENTO! Tente novamente!')

print(f'Sua compra de R${valorCompra:,.2f} vai custar R${totalCompra:,.2f} no final')
