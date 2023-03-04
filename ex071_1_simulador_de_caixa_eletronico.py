# simulador de caixa eletronico

print('=' * 50)
print(f'{"BANCO CAPELA":^50}')
print('=' * 50)
valor = int(input('Qual valor voce quer sacar? R$'))
total = valor
cedula = 50
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cedula(s) de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break

print('=' * 50)
print(f'Volte sempre ao BANCO CAPELA! Tenha um bom dia!')
