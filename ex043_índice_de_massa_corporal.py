# Calculo de IMC
titulo = 'Calculador de ICM'
print('-='*20)
print('{:^40}'.format(titulo))
print('-='*20)
peso = float(input('Qual e seu peso? (Kg) '))
altura = float(input('Qual e sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa e de {imc:.1f}')

if imc < 18.5:
    print(f'Voce esta em ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print(f'PARABENS, voce esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print(f'Voce esta em SOBREPESO!')
elif 30 <= imc < 40:
    print(f'Voce esta em OBESIDADE!')
else:
    print(f'Voce esta em OBESIDADE MORBIDA, cuidado!')
