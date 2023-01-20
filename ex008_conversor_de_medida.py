# imprime a conversão do valor digitado em metros para centímetros e milímetros

medidaMetros = float(input('Qual a medida em metros: '))
print('{}m equivale: {:>10,.1f}cm'.format(medidaMetros, medidaMetros * 100))
print('{}m equivale: {:>10,.1f}mm'.format(medidaMetros, medidaMetros * 1000))