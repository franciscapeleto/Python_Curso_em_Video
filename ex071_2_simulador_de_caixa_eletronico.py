# simulador de caixa eletronico

print('=' * 50)
print(f'{"BANCO CAPELA":^50}')
print('=' * 50)
valor = int(input('Qual valor voce quer sacar? R$'))
cinquenta = vinte = dez = um = 0

while True:
    if valor >= 50:
        cinquenta = valor // 50
        valor -= cinquenta * 50
        print(f'total de {cinquenta} cedulas de R$50.00')
    elif valor >= 20:
        vinte = valor // 20
        valor -= vinte * 20
        print(f'total de {vinte} cedulas de R$20.00')
    elif valor >= 10:
        dez = valor // 10
        valor -= dez * 10
        print(f'total de {dez} cedulas de R$10.00')
    elif valor > 0:
        um = valor
        valor -= um
        print(f'total de {um} cedulas de R$1.00')
    else:
        break

print('=' * 50)
print(f'Volte sempre ao BANCO CAPELA! Tenha um bom dia!')
