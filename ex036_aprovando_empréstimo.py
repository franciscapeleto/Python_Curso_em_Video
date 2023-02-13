# Analisa se o usuario podera financiar uma casa e qual sera a parcela
valorCasa = float(input('Valor da casa: R$'))
salarioComprador = float(input('Salario do comprador: R$'))
anosFinanciamento = int(input('Quantos anos de financiamento? '))
prestacao = valorCasa / (anosFinanciamento * 12)
print(f'\nPara pagar uma casa de R${valorCasa:,.2f} em {anosFinanciamento} anos\n'
      f'a prestacao sera de R${prestacao:,.2f} por mes')

if prestacao / salarioComprador > 0.3:
    print(f'\nEmprestimo NEGADO!')
else:
    print(f'\nEmprestimo pode ser CONCEDIDO!')
