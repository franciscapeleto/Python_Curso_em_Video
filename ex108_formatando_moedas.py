# mostra diferente valores com base em um valor escolhido pelo usuario

from ex108 import moeda

p = float(input('Digite o preco: R$ '))
m = int(input('Qual moeda voce deseja? [1=Real / 2=Dolar] '))
print(f'A metade de {moeda.moeda(p, m)} e {moeda.moeda(moeda.metade(p), m)}')
print(f'O dobro de {moeda.moeda(p, m)} e {moeda.moeda(moeda.dobro(p), m)}')
print(f'Aumentando 10% de {moeda.moeda(p, m)}, temos {moeda.moeda(moeda.aumentar(p, 10), m)}')
print(f'Reduzindo 13% de {moeda.moeda(p, m)}, temos {moeda.moeda(moeda.diminuir(p, 13), m)}')
