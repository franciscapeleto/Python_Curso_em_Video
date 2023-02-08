# Analisa se tres segmentos de reta podem formar um triangulo
titulo = 'Analisador de Triangulo'
print('-='*20)
print('{:^40}'.format(titulo))
print('-='*20)
segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 + segmento2 > segmento3 and segmento1 + segmento3 > segmento2 and segmento2 + segmento3 > segmento1:
    print('Os segmentos acima PODEM FORMAR triangulo!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo!')
