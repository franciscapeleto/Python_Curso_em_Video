# mostra diferente valores com base em um valor escolhido pelo usuario

from ex107 import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de R${p:,.2f} e R${moeda.metade(p):,.2f}')
print(f'O dobro de R${p:,.2f} e R${moeda.dobro(p):,.2f}')
print(f'Aumentando 10% de R${p:,.2f}, temos R${moeda.aumentar(p, 10):,.2f}')
print(f'Reduzindo 13% de R${p:,.2f}, temos R${moeda.diminuir(p, 13):,.2f}')
