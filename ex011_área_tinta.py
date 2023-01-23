# calcula a área da parede e a quantidade de tinta necessária para pintar a parede

largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? ' ))
m2 = largura * altura
tinta = m2 / 2
print('A área da parede é de {}m2 a qual é necessário {}l de tinta para pintar a parede.'.format(m2, tinta))
