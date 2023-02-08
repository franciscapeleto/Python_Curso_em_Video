# Calcula o aumento do salario do funcionario
salario = float(input('Qual e o salario do funcionario? R$'))

if salario > 1250:
    salarioNovo = salario * 1.1
else:
    salarioNovo = salario * 1.15

print(f'Quem ganhava R${salario:,.2f} passa a ganhar R${salarioNovo:,.2f} agora.')
