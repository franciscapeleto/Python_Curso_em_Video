# calcula o valor total de locação de um carro

dias = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos Km foram rodados? '))
valor_Dia = dias * 60
valor_Km = km * 0.15
print('O valor total a pagar pela locação do carro é de R${:,.2f}.'.format(valor_Dia + valor_Km))
