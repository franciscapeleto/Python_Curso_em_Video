# calcula o valor da hipotenusa

from math import hypot
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
